from app import db, ma

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    qty = db.Column(db.Integer)

    def __init__(self, Name, description, qty):
        self.Name = Name
        self.description = description
        self.qty = qty

class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'Name', 'description', 'qty')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)