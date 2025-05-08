import decimal


def query_to_list(query_result):
    """Converts a SQLAlchemy query result to a list of dictionaries, excluding internal fields like _sa_instance_state."""
    return [
        {key: value for key, value in record.__dict__.items() if not key.startswith('_')} 
        for record in query_result
    ]
def convert_to_json_serializable(query_result):
    """Converts a SQLAlchemy query result to a list of dictionaries with JSON serializable values."""
    result = []
    for record in query_result:
        record_dict = {}
        for key, value in record.__dict__.items():
            if not key.startswith('_'):
                # Handle Decimal objects
                if isinstance(value, decimal.Decimal):
                    record_dict[key] = float(value)
                else:
                    record_dict[key] = value
        result.append(record_dict)
    return result