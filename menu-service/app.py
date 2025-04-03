from flask import Flask, request, jsonify
from database import db
from models import Restaurant, MenuItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
db.init_app(app)

@app.route("/restaurants", methods=["POST"])
def add_restaurant():
    data = request.json
    r = Restaurant(name=data["name"], location=data["location"])
    db.session.add(r)
    db.session.commit()
    return jsonify({"message": "Restaurant added!"})

@app.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "location": r.location} for r in restaurants])

@app.route("/restaurants/<int:id>/menu", methods=["GET", "POST"])
def menu_items(id):
    if request.method == "GET":
        items = MenuItem.query.filter_by(restaurant_id=id).all()
        return jsonify([
            {"id": i.id, "name": i.name, "price": i.price}
            for i in items
        ])
    else:
        data = request.json
        item = MenuItem(
            name=data["name"],
            price=data["price"],
            restaurant_id=id
        )
        db.session.add(item)
        db.session.commit()
        return jsonify({"message": "Menu item added!"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

