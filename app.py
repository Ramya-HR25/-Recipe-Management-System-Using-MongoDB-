from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["recipe_db"]
recipes = db["recipes"]

@app.route("/")
def home():
    all_recipes = list(recipes.find())
    return render_template("index.html", recipes=all_recipes)

@app.route("/add", methods=["POST"])
def add():
    recipes.insert_one({
        "name": request.form["name"],
        "ingredients": request.form["ingredients"],
        "steps": request.form["steps"]
    })
    return redirect("/")

@app.route("/delete/<id>")
def delete(id):
    recipes.delete_one({"_id": ObjectId(id)})
    return redirect("/")

@app.route("/update/<id>", methods=["POST"])
def update(id):
    recipes.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "name": request.form["name"],
            "ingredients": request.form["ingredients"],
            "steps": request.form["steps"]
        }}
    )
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)