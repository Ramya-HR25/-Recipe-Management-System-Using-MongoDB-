"""
Interactive MongoDB Script for Recipe App
Run this script to interact with the recipe database directly.
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["recipe_db"]
recipes_collection = db["recipes"]

def show_menu():
    """Display the menu options"""
    print("\n" + "="*50)
    print("RECIPE DATABASE MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Show all recipes")
    print("2. Add a new recipe")
    print("3. Find a recipe by ID")
    print("4. Update a recipe")
    print("5. Delete a recipe")
    print("6. Count total recipes")
    print("7. Delete all recipes (CAUTION!)")
    print("8. Exit")
    print("="*50)

def show_all_recipes():
    """Show all recipes in the database"""
    print("\n--- ALL RECIPES ---")
    recipes = list(recipes_collection.find())
    if not recipes:
        print("No recipes found.")
        return
    
    for i, recipe in enumerate(recipes, 1):
        print(f"\n{i}. ID: {recipe['_id']}")
        print(f"   Name: {recipe['name']}")
        print(f"   Ingredients: {recipe['ingredients']}")
        print(f"   Steps: {recipe['steps']}")

def add_recipe_interactive():
    """Add a new recipe through interactive input"""
    print("\n--- ADD NEW RECIPE ---")
    name = input("Recipe Name: ").strip()
    if not name:
        print("Recipe name cannot be empty!")
        return
    
    ingredients = input("Ingredients: ").strip()
    steps = input("Preparation Steps: ").strip()
    
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "steps": steps
    }
    
    result = recipes_collection.insert_one(recipe)
    print(f"✅ Recipe added successfully with ID: {result.inserted_id}")

def find_recipe_by_id_interactive():
    """Find a recipe by ID through interactive input"""
    print("\n--- FIND RECIPE BY ID ---")
    recipe_id = input("Enter Recipe ID: ").strip()
    if not recipe_id:
        print("Recipe ID cannot be empty!")
        return
    
    try:
        obj_id = ObjectId(recipe_id)
        recipe = recipes_collection.find_one({"_id": obj_id})
        if recipe:
            print(f"\n🔍 Found Recipe:")
            print(f"   ID: {recipe['_id']}")
            print(f"   Name: {recipe['name']}")
            print(f"   Ingredients: {recipe['ingredients']}")
            print(f"   Steps: {recipe['steps']}")
        else:
            print("❌ Recipe not found.")
    except Exception as e:
        print(f"❌ Invalid ID format: {e}")

def update_recipe_interactive():
    """Update a recipe through interactive input"""
    print("\n--- UPDATE RECIPE ---")
    recipe_id = input("Enter Recipe ID to update: ").strip()
    if not recipe_id:
        print("Recipe ID cannot be empty!")
        return
    
    try:
        obj_id = ObjectId(recipe_id)
        recipe = recipes_collection.find_one({"_id": obj_id})
        if not recipe:
            print("❌ Recipe not found.")
            return
        
        print(f"\nCurrent values:")
        print(f"Name: {recipe['name']}")
        print(f"Ingredients: {recipe['ingredients']}")
        print(f"Steps: {recipe['steps']}")
        
        # Get new values
        print("\nEnter new values (press Enter to keep current value):")
        new_name = input(f"New Name [{recipe['name']}]: ").strip()
        new_ingredients = input(f"New Ingredients [{recipe['ingredients']}]: ").strip()
        new_steps = input(f"New Steps [{recipe['steps']}]: ").strip()
        
        # Prepare update fields
        update_fields = {}
        if new_name:
            update_fields["name"] = new_name
        if new_ingredients:
            update_fields["ingredients"] = new_ingredients
        if new_steps:
            update_fields["steps"] = new_steps
        
        if not update_fields:
            print("No changes made.")
            return
            
        result = recipes_collection.update_one(
            {"_id": obj_id},
            {"$set": update_fields}
        )
        
        if result.modified_count > 0:
            print("✅ Recipe updated successfully.")
        else:
            print("ℹ️ No changes made.")
            
    except Exception as e:
        print(f"❌ Error updating recipe: {e}")

def delete_recipe_interactive():
    """Delete a recipe through interactive input"""
    print("\n--- DELETE RECIPE ---")
    recipe_id = input("Enter Recipe ID to delete: ").strip()
    if not recipe_id:
        print("Recipe ID cannot be empty!")
        return
    
    try:
        obj_id = ObjectId(recipe_id)
        recipe = recipes_collection.find_one({"_id": obj_id})
        if not recipe:
            print("❌ Recipe not found.")
            return
        
        print(f"\nRecipe to delete:")
        print(f"Name: {recipe['name']}")
        confirm = input("\n⚠️ Are you sure you want to delete this recipe? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            result = recipes_collection.delete_one({"_id": obj_id})
            if result.deleted_count > 0:
                print("✅ Recipe deleted successfully.")
            else:
                print("❌ Failed to delete recipe.")
        else:
            print("❌ Deletion cancelled.")
            
    except Exception as e:
        print(f"❌ Error deleting recipe: {e}")

def count_recipes():
    """Count total number of recipes"""
    count = recipes_collection.count_documents({})
    print(f"\n📊 Total recipes in database: {count}")
    return count

def delete_all_recipes_interactive():
    """Delete all recipes with confirmation"""
    print("\n--- DELETE ALL RECIPES ---")
    count = recipes_collection.count_documents({})
    if count == 0:
        print("No recipes to delete.")
        return
    
    print(f"⚠️ You are about to delete ALL {count} recipes!")
    confirm = input("Type 'DELETE ALL' to confirm: ").strip()
    
    if confirm == 'DELETE ALL':
        result = recipes_collection.delete_many({})
        print(f"✅ Deleted {result.deleted_count} recipes.")
    else:
        print("❌ Deletion cancelled.")

def main():
    """Main interactive loop"""
    print("Welcome to the Recipe Database Management System!")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            show_all_recipes()
        elif choice == '2':
            add_recipe_interactive()
        elif choice == '3':
            find_recipe_by_id_interactive()
        elif choice == '4':
            update_recipe_interactive()
        elif choice == '5':
            delete_recipe_interactive()
        elif choice == '6':
            count_recipes()
        elif choice == '7':
            delete_all_recipes_interactive()
        elif choice == '8':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-8.")
        
        # Pause to let user read output
        if choice != '8':
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()