from flask import Flask, request, jsonify
from database import db
from models import CartItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cart.db'
db.init_app(app)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.json
    item = CartItem(
        user_email=data["user_email"],
        item_name=data["item_name"],
        price=data["price"],
        quantity=data["quantity"]
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({"message": "Item added to cart!"})

@app.route("/cart/<string:user_email>", methods=["GET"])
def view_cart(user_email):
    items = CartItem.query.filter_by(user_email=user_email).all()
    return jsonify([
        {
            "id": i.id,
            "item_name": i.item_name,
            "price": i.price,
            "quantity": i.quantity
        } for i in items
    ])

@app.route("/cart/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):
    item = CartItem.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item removed from cart"})
    else:
        return jsonify({"message": "Item not found"}), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
