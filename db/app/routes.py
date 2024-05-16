# app/routes.py
from flask import Blueprint, jsonify, current_app,request
import threading
from .database import fetch_data
from .decorators import with_database_query

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/', methods=['GET'])
def get_default_function():
    return 'Hello, World!'

@api_blueprint.route('/getCompanyList', methods=['GET'])
@with_database_query()
def get_company_list():
    return f"SELECT * FROM Companies LIMIT 10"
   
@api_blueprint.route('/getCompanyDetailById', methods=['GET'])
@with_database_query()
def get_company_detail_by_id():
    company_id = request.args.get('id', type=int)
    if not company_id:
        return jsonify({"error": "Missing company ID"}), 400
    return f"SELECT * FROM Companies WHERE id = {company_id}"
  
@api_blueprint.route('/getCustomerList', methods=['GET'])
@with_database_query()
def get_customer_list():
    return f"SELECT * FROM Customers LIMIT 10"

@api_blueprint.route('/getCustomerDetailById', methods=['GET'])
def get_customer_details():
    customer_id = request.args.get('id', type=int)
    if not customer_id:
        return jsonify({"error": "Missing customer ID"}), 400
    return f"SELECT * FROM Customers WHERE id = {customer_id}"
   
   

