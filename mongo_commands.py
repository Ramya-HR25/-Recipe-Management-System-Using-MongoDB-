"""
MongoDB Commands for Recipe App
This script demonstrates how to interact with MongoDB directly using Python.
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["recipe_db"]
recipes_collection = db["recipes"]

def show_all_recipes():
    """Show all recipes in the database"""
    print("=== ALL RECIPES ===")
    recipes = list(recipes_collection.find())
    if not recipes:
        print("No recipes found.")
        return
    
    for recipe in recipes:
        print(f"\nID: {recipe['_id']}")
        print(f"Name: {recipe['name']}")
        print(f"Ingredients: {recipe['ingredients']}")
        print(f"Steps: {recipe['steps']}")
        print("-" * 40)

def add_recipe(name, ingredients, steps):
    """Add a new recipe to the database"""
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "steps": steps
    }
    result = recipes_collection.insert_one(recipe)
    print(f"Recipe added with ID: {result.inserted_id}")
    return result.inserted_id

def find_recipe_by_id(recipe_id):
    """Find a recipe by its ID"""
    try:
        obj_id = ObjectId(recipe_id)
        recipe = recipes_collection.find_one({"_id": obj_id})
        if recipe:
            print(f"\nFound Recipe:")
            print(f"ID: {recipe['_id']}")
            print(f"Name: {recipe['name']}")
            print(f"Ingredients: {recipe['ingredients']}")
            print(f"Steps: {recipe['steps']}")
        else:
            print("Recipe not found.")
        return recipe
    except Exception as e:
        print(f"Invalid ID format: {e}")
        return None

def update_recipe(recipe_id, name=None, ingredients=None, steps=None):
    """Update a recipe"""
    try:
        obj_id = ObjectId(recipe_id)
        update_fields = {}
        if name:
            update_fields["name"] = name
        if ingredients:
            update_fields["ingredients"] = ingredients
        if steps:
            update_fields["steps"] = steps
            
        result = recipes_collection.update_one(
            {"_id": obj_id},
            {"$set": update_fields}
        )
        
        if result.modified_count > 0:
            print("Recipe updated successfully.")
        else:
            print("No changes made or recipe not found.")
    except Exception as e:
        print(f"Error updating recipe: {e}")

def delete_recipe(recipe_id):
    """Delete a recipe by ID"""
    try:
        obj_id = ObjectId(recipe_id)
        result = recipes_collection.delete_one({"_id": obj_id})
        if result.deleted_count > 0:
            print("Recipe deleted successfully.")
        else:
            print("Recipe not found.")
    except Exception as e:
        print(f"Error deleting recipe: {e}")

def delete_all_recipes():
    """Delete all recipes (use with caution!)"""
    result = recipes_collection.delete_many({})
    print(f"Deleted {result.deleted_count} recipes.")

def count_recipes():
    """Count total number of recipes"""
    count = recipes_collection.count_documents({})
    print(f"Total recipes: {count}")
    return count

# Example usage
if __name__ == "__main__":
    print("MongoDB Recipe Database Commands")
    print("=" * 40)
    
    # Show current recipes
    show_all_recipes()
    
    # Count recipes
    count_recipes()
    
    print("\n" + "=" * 40)
    print("Example commands you can run:")
    print("1. show_all_recipes()")
    print("2. add_recipe('Pasta', 'Pasta, Sauce, Cheese', 'Boil pasta, add sauce, add cheese')")
    print("3. find_recipe_by_id('your_recipe_id')")
    print("4. update_recipe('recipe_id', name='New Name')")
    print("5. delete_recipe('recipe_id')")
    print("6. count_recipes()")