from flask import Blueprint, jsonify, request
import random
from app.utils import get_quote_from_category

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/quote', methods=['GET'])
def get_random_quote():
    category = request.args.get('category', 'motivational')

    quote_data = get_quote_from_category(category)

    return jsonify(quote_data)
