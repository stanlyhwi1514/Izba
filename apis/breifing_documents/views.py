from flask import Blueprint, request, jsonify, g
from jsonschema import validate, ValidationError
from mongo_schemas.breifing_document import breifing_document_schema
from mongo_validator.validate_json import validate_json
from apis.common_model.models import Customer
from apis.AlwaysOnChannel.models import Alert
from common.utils.object_convertor import query_to_list
from apis.common_model.models import User
from extensions import mongo




briefing_api = Blueprint('briefing', __name__)


@briefing_api.route('/v1/briefing/addBriefingDocument', methods=['POST'])
@validate_json(breifing_document_schema)
def insert_briefing_document():
    try:

        data = request.get_json()

        # Use MongoDB collection from tenant-specific DB
        collection = g.mongo_db["briefin_documents"]
        result = collection.insert_one(data)

        return jsonify({
            "message": "Document inserted successfully",
            "id": str(result.inserted_id)
        }), 201

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500
    


@briefing_api.route('/v1/briefing/getRisk', methods=['GET'])
def getRisk():
    try:
        db = g.db  # ✅ get the session instance

        customer_id = request.args.get('customer_id')

        if customer_id:
            customer = db.query(Customer).filter(Customer.id == customer_id).first()
            if not customer:
                return jsonify({'error': 'Customer not found'}), 404

            # Filter related alerts with type = 'risk'
            alerts = [alert for alert in customer.alerts if alert.type == 'Risk']
        else:
            # Query all alerts with type = 'risk'
            alerts = db.query(Alert).filter(Alert.type == 'Risk').all()

        result = query_to_list(alerts)
        return jsonify({'alerts': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@briefing_api.route('/v1/briefing/getOpportunity', methods=['GET'])
def getOpportunity():
    try:
        db = g.db  # ✅ get the session instance

        customer_id = request.args.get('customer_id')

        if customer_id:
            customer = db.query(Customer).filter(Customer.id == customer_id).first()
            if not customer:
                return jsonify({'error': 'Customer not found'}), 404

            # Filter related alerts with type = 'risk'
            alerts = [alert for alert in customer.alerts if alert.type == 'Opportunity']
        else:
            # Query all alerts with type = 'risk'
            alerts = db.query(Alert).filter(Alert.type == 'Opportunity').all()

        result = query_to_list(alerts)
        return jsonify({'alerts': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@briefing_api.route('/v1/briefing/getAccountsTeam', methods=['GET'])
def getAccountsTeam():
    try:
        db = g.db  # ✅ get the session instance

        # Optional: filter by customer_id if needed
        customer_id = request.args.get('customer_id')

        query = db.query(User).filter(User.user_type == 'accounts')

        if customer_id:
            query = query.filter(User.customer_id == customer_id)

        users = query.all()
        result = [{
            'id': user.id,
            'email': user.email,
            'full_name': user.full_name,
            'user_type': user.user_type,
            'is_active': user.is_active
        } for user in users]

        return jsonify({'accounts_team': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@briefing_api.route('/v1/briefing/getCustomerTeam', methods=['GET'])
def getCustomerTeam():
    try:
        db = g.db  # ✅ get the session instance

        # Optional: filter by customer_id if needed
        customer_id = request.args.get('customer_id')

        query = db.query(User).filter(User.user_type == 'customer')

        if customer_id:
            query = query.filter(User.customer_id == customer_id)

        users = query.all()
        result = [{
            'id': user.id,
            'email': user.email,
            'full_name': user.full_name,
            'user_type': user.user_type,
            'is_active': user.is_active
        } for user in users]

        return jsonify({'accounts_team': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@briefing_api.route('/v1/briefing/getPlaybook', methods=['GET'])
def getPlayBook():
    try:
        # Fetch all documents from the "playbook" collection
        playbooks_cursor = mongo.db.playbook.find()
        
        # Convert the cursor to a list of dictionaries
        playbooks = query_to_list(playbooks_cursor)  # or use list(playbooks_cursor) if you don’t need custom conversion
        
        return jsonify({
            "success": True,
            "data": playbooks
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500