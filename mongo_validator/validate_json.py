from functools import wraps
from flask import request, jsonify
from jsonschema import validate, ValidationError

def validate_json(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                data = request.get_json()
                if data is None:
                    raise ValidationError("Missing JSON in request")
                validate(instance=data, schema=schema)
            except ValidationError as e:
                return jsonify({"error": str(e.message)}), 400
            return f(*args, **kwargs)
        return wrapper
    return decorator
