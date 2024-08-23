from flask import Blueprint,jsonify,request
from controllers.customerController import save,find_all,login

customer_blueprint = Blueprint('customer_bp',__name__)

customer_blueprint.route('/',methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
# need to add find_all_paginate

customer_blueprint.route('/login',methods=['POST'])(login)

