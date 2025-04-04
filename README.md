# 🍽️ MicroZomato

A mini food ordering system built using Python Flask and Microservices architecture.  
It includes separate services for user authentication, menu management, cart operations, and order placement.

---

## 🚀 Features

✅ User Registration & Login  
✅ View Restaurant Menus  
✅ Add Items to Cart  
✅ Place Orders  
✅ Microservice-based Design  
✅ Tested with `curl` (CLI) – Postman-compatible

---

## 🧱 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite (Local DB)
- cURL for API testing

---

## 📦 Microservices Structure


Each folder has:
- `app.py` (Flask server)
- `models.py` (SQLAlchemy models)
- `database.py` (DB config)
- `requirements.txt` and `.gitignore`

---

## 🏁 How to Run It Locally

Step-by-step instructions to run each service and test APIs:  
📄 [run_instructions.md](./run_instructions.md)

---

## 🧪 Sample API Calls (cURL)

```bash
# Sign Up
curl -X POST http://127.0.0.1:5000/signup -H "Content-Type: application/json" -d "{\"name\":\"Ravi\", \"email\":\"ravi@foodie.com\", \"password\":\"1234\"}"

# Add to Cart
curl -X POST http://127.0.0.1:5000/cart -H "Content-Type: application/json" -d "{\"user_email\":\"ravi@foodie.com\", \"item_name\":\"Pizza\", \"price\":299, \"quantity\":1}"

# Place Order
curl -X POST http://127.0.0.1:5000/order -H "Content-Type: application/json" -d "{\"user_email\":\"ravi@foodie.com\", \"items\":[{\"item_name\":\"Pizza\", \"price\":299, \"quantity\":1}]}"


---

## ✅ Step 3: Save, Add, Commit, and Push

```bash
git add README.md
git commit -m "Added README.md with project overview and instructions"
git push
