from flask import Blueprint, request, jsonify, Response, g
from extensions import mongo
from common.utils.object_convertor import query_to_list  # assuming this converts a MongoDB cursor to a list

playbook_api = Blueprint('playbook', __name__)

@playbook_api.route('/v1/playbook/getPlayBook', methods=['GET'])
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