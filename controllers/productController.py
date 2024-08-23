from flask import jsonify,request
from models.schemas.productSchema import product_schema,products_schema 
from marshmallow import ValidationError
from services import productService
from utils.util import user_token_wrapper,token_required

def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.message),400
    
    try:
        product_save = productService.save(product_data)
        return product_schema.jsonify(product_save),201
    except ValidationError as e:
        return jsonify({"error":str(e)}),400

@token_required
def find_all():
    all_products = productService.find_all()
    return products_schema.jsonify(all_products),200    
    
def search_product():
    search_term = request.args.get("search")
    searched_item = productService.search_product(search_term)
    return products_schema.jsonify(searched_item)

    #www.127.0.0.1:5000/search_songs?song=Old Town Road
