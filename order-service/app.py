from flask import Flask, request, jsonify
from database import db
from models import Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db.init_app(app)

@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    for item in data["items"]:
        order = Order(
            user_email=data["user_email"],
            item_name=item["item_name"],
            quantity=item["quantity"],
            total_price=item["price"] * item["quantity"]
        )
        db.session.add(order)
    db.session.commit()
    return jsonify({"message": "Order placed successfully!"})

@app.route("/order/<string:user_email>", methods=["GET"])
def view_orders(user_email):
    orders = Order.query.filter_by(user_email=user_email).all()
    return jsonify([
        {
            "item_name": o.item_name,
            "quantity": o.quantity,
            "total_price": o.total_price
        } for o in orders
    ])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
