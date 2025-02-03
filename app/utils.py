import random
import json

def load_quotes():
    with open('app/quotes.json', 'r') as file:
        return json.load(file)

def get_quote_from_category(category):
    quotes = load_quotes()
    category_quotes = quotes.get(category.lower(), quotes['motivational'])
    return {"quote": random.choice(category_quotes), "category": category}
