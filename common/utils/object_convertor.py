def query_to_list(query_result):
    """Converts a SQLAlchemy query result to a list of dictionaries, excluding internal fields like _sa_instance_state."""
    return [
        {key: value for key, value in record.__dict__.items() if not key.startswith('_')} 
        for record in query_result
    ]