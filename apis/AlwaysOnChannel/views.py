from flask import Blueprint, request, jsonify
from extensions import db
from common.utils.object_convertor import query_to_list

from apis.common_model.models import Customer

from apis.AlwaysOnChannel.models import Alert
from flask import Response, g



channel_api = Blueprint('channel', __name__)

@channel_api.route('/v1/channel/getCustomers', methods=['GET'])
def getCustomers():
    try:
        db = g.db
        filter_by = request.args.get("filter")  # Correct way to get query param

        query = db.query(Customer)

        if filter_by:
            if filter_by == "renewal_date":
                query = query.order_by(Customer.renewal_date.asc())
            elif filter_by == "net_revenue_retention":
                query = query.order_by(Customer.net_revenue_retention.desc())
            elif filter_by == "high_revenue":
                query = query.order_by(Customer.total_revenue.desc())
            elif filter_by == "low_revenue":
                query = query.order_by(Customer.total_revenue.asc())
            
        else:
            customers = query.all()

        result = query_to_list(customers)  # Convert result to list of dicts
        return jsonify({'categories': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@channel_api.route('/v1/channel/CreateAlerts', methods=['POST'])
def create_alert():
    db=g.db
    data = request.get_json()

    required_fields = ['customer_id', 'type', 'severity']

    # Check if all required fields are present
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    # Create an Alert object
    new_alert = Alert(
        customer_id=data['customer_id'],
        type=data['type'],
        severity=data['severity'],
        title=data.get('title'),          # optional
        message=data.get('message'),      # optional
        raised_by=data.get('raised_by'),  # optional
        is_new=data.get('is_new', True)   # optional, default True
    )

    try:
        db.add(new_alert)  # Use db.add instead of db.session.add
        db.commit()        # Use db.commit instead of db.session.commit
        return jsonify({'message': 'Alert created successfully'}), 201
    except Exception as e:
        db.rollback() 
        return jsonify({'error': str(e)}), 500


from flask import g

@channel_api.route('/v1/channel/getAlerts', methods=['GET'])
def getAlerts():
    try:
        db = g.db  # ✅ get the session instance

        customer_id = request.args.get('customer_id')

        if customer_id:
            customer = db.query(Customer).filter(Customer.id == customer_id).first()
            if not customer:
                return jsonify({'error': 'Customer not found'}), 404

            alerts = customer.alerts  # Uses the defined relationship
        else:
            alerts = db.query(Alert).all()

        result = query_to_list(alerts)
        return jsonify({'alerts': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
