from flask import Blueprint, request, jsonify
from extensions import db
from flask import g
from apis.Chat.models import Category, Prompt,FocusCategory  # Assuming these are your models
from common.utils.object_convertor import query_to_list
from  apis.common_model.models import Customer
chat_api = Blueprint('chat_api', __name__)

@chat_api.route('/v1/chat/insertCategories', methods=['POST'])
def insert_data():
    try:
        # Get data from the POST request
        data = request.get_json()
        
        # Ensure the necessary fields are in the data
        if 'name' not in data or 'display_order' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Create a new Category instance with the data from the request
        category = Category(
            name=data['name'],
            display_order=data['display_order']
        )
        
        # Add the new category to the session and commit it to the database
        db.session.add(category)
        db.session.commit()

        # Return a success message along with the inserted category's details
        return jsonify({
            'message': 'Category inserted successfully',
            'category': {
                'name': category.name,
                'display_order': category.display_order,
                'created_at': category.created_at
            }
        }), 201

    except Exception as e:
        # Handle any errors
        db.session.rollback()  # Rollback any changes in case of an error
        return jsonify({'error': str(e)}), 500


@chat_api.route('/v1/chat/insertPrompt', methods=['POST'])
def insert_prompt():
    try:
        # Get data from the POST request
        data = request.get_json()

        # Ensure the necessary fields are in the data
        if 'category_id' not in data or 'text' not in data or 'display_order' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        # Validate category_id format
        try:
            category_id = data['category_id']
        except ValueError:
            return jsonify({'error': 'Invalid category_id format'}), 400

        # Check if the category exists
        category = Category.query.filter_by(id=category_id).first()
        if not category:
            return jsonify({'error': 'Category not found'}), 404

        # Create a new Prompt instance with the data from the request
        prompt = Prompt(
            category_id=category_id,
            text=data['text'],
            display_order=data['display_order']
        )
        
        # Add the new prompt to the session and commit it to the database
        db.session.add(prompt)
        db.session.commit()

        # Return a success message along with the inserted prompt's details
        return jsonify({
            'message': 'Prompt inserted successfully',
            'prompt': {
                'category_id': str(prompt.category_id),
                'text': prompt.text,
                'display_order': prompt.display_order,
                'created_at': prompt.created_at
            }
        }), 201

    except Exception as e:
        # Handle any errors
        db.session.rollback()  # Rollback any changes in case of an error
        return jsonify({'error': str(e)}), 500
    

@chat_api.route('/v1/chat/getPromptsByCategory/<category_id>', methods=['GET'])
def get_prompts_by_category(category_id):
    try:
        # Validate category_id format
        try:
            category_uuid = category_id
        except ValueError:
            return jsonify({'error': 'Invalid category_id format'}), 401

        # Fetch the category from the database
        category = Category.query.filter_by(id=category_uuid).first()
        if not category:
            return jsonify({'error': 'Category not found'}), 404

        # Fetch all prompts associated with the category
        prompts = Prompt.query.filter_by(category_id=category_uuid).all()

        # If no prompts are found for the category
        if not prompts:
            return jsonify({'message': 'No prompts found for this category'}), 404

        # Prepare the list of prompts for the response
        prompts_data = [
            {
                'category_id': str(prompt.category_id),
                'text': prompt.text,
                'display_order': prompt.display_order,
                'created_at': prompt.created_at
            }
            for prompt in prompts
        ]

        # Return the list of prompts
        return jsonify([{
            'category_id': str(category.id),
            'category_name': category.name,
            'prompts': prompts_data
        }]), 200

    except Exception as e:
        # Handle any errors
        return jsonify({'error': str(e)}), 500

@chat_api.route('/v1/chat/insertFocusCategory', methods=['POST'])
def insert_focus_category():
    try:
        # Get data from the POST request
        data = request.get_json()

        # Ensure necessary fields are provided
        if 'name' not in data or 'display_order' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new FocusCategory instance with the data from the request
        focus_category = FocusCategory(
            name=data['name'],
            display_order=data['display_order']
        )
        
        # Add the new category to the session and commit it to the database
        db.session.add(focus_category)
        db.session.commit()

        # Return a success message along with the inserted FocusCategory's details
        return jsonify({
            'message': 'FocusCategory inserted successfully',
            'focus_category': {
                'id': str(focus_category.id),
                'name': focus_category.name,
                'display_order': focus_category.display_order,
                'created_at': focus_category.created_at
            }
        }), 201

    except Exception as e:
        # Handle any errors and rollback in case of an exception
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@chat_api.route('/v1/chat/getFocusCategories', methods=['GET'])
def get_focus_categories():
    try:
        # Fetch all categories from the database
        categories = FocusCategory.query.all()

        # Convert the query result to a list of dictionaries
        result = query_to_list(categories)

        # Check if categories exist
        if not result:
            return jsonify({'message': 'No categories found'}), 404

        # Return the categories as JSON
        return jsonify({'categories': result}), 200

    except Exception as e:
        # Handle any errors
        return jsonify({'error': str(e)}), 500
    
@chat_api.route('/v1/channel/getCustomers', methods=['GET'])
def getCustomers():
    try:
        # Use the db session stored in g
        db = g.db

        # Query all customers using the g.db session
        customers = db.query(Customer).all()

        # Assuming query_to_list is a function to convert the result to a dictionary
        result = query_to_list(customers)

        return jsonify({'categories': result}), 200

    except Exception as e:
        return jsonify({'some thing went wrong': str(e)}), 500



#checking commit 
#checking commit 2