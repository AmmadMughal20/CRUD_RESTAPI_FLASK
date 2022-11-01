from app import app,db
from flask import request
from app.models import Products, product_schema, products_schema

@app.route('/product', methods=['POST'])
def add_product():

    Name = request.json['name']
    description = request.json['description']
    qty = request.json['qty']

    new_Product = Products(Name, description, qty)

    db.session.add(new_Product)
    db.session.commit()

    return product_schema.jsonify(new_Product)

@app.route('/product', methods=['GET'])
def get_products():
    all_products = Products.query.all()
    result = products_schema.dump(all_products)
    return products_schema.jsonify(result)

@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Products.query.get(id)
    return product_schema.jsonify(product)

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Products.query.get(id)

    Name = request.json['name']
    description = request.json['description']
    qty = request.json['qty']

    product.Name = Name
    product.description = description
    product.qty = qty

    db.session.commit()
    return product_schema.jsonify(product)

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Products.query.get(id)
    db.session.delete(product)

    db.session.commit()
    return product_schema.jsonify(product)