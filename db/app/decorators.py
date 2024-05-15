from functools import wraps
from flask import Blueprint, jsonify, current_app
import threading
from .database import fetch_data

def fetch_data_thread(query, result_container, app_context):
    with app_context:
        data, error = fetch_data(query)
        result_container.append((data, error))

def make_response(data=None, error=None, status_code=200):
    if error:
        response = {
            "success": False,
            "error": {
                "message": str(error),
                "type": type(error).__name__
            }
        }
        return jsonify(response), status_code
    else:
        response = {
            "success": True,
            "data": data
        }
        return jsonify(response), status_code        

def with_database_query():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            query = f(*args, **kwargs)
            result_container = []
            app_context = current_app.app_context()
            query_thread = threading.Thread(target=fetch_data_thread, args=(query, result_container, app_context))
            query_thread.start()
            query_thread.join(timeout=15)

            if query_thread.is_alive():
                return make_response(error="Query timeout", status_code=504)

            if not result_container:
                return make_response(error="No result returned", status_code=404)

            data, error = result_container[0]
            if error:
                return make_response(error=error, status_code=500)
            
            return make_response(data=data)
        return decorated_function
    return decorator
