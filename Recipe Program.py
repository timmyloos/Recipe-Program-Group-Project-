# Define the ingredients for each recipe
recipes = {
    "chocolate cake": {
        "flour": 250, "grams"
        "sugar": 200,
        "cocoa powder": 50,
        "baking powder": 2,
        "baking soda": 1,
        "salt": 1,
        "eggs": 2,
        "milk": 120,
        "vegetable oil": 60,
        "vanilla extract": 2,
        "hot water": 120
    },
    "chicken alfredo": {
        "spaghetti": 16,
        "chicken breast": 1,
        "olive oil": 2,
        "garlic": 2,
        "heavy cream": 2,
        "parmesan cheese": 0.5,
        "salt": 1,
        "pepper": 1
    },
    "vegetable stir-fry": {
        "rice": 2,
        "soy sauce": 1,
        "cornstarch": 1,
        "sesame oil": 1,
        "garlic": 2,
        "ginger": 1,
        "carrots": 2,
        "broccoli": 2,
        "red bell pepper": 1,
        "snow peas": 1,
        "water chestnuts": 1,
        "green onions": 1
    },
    "lasagna": {
        "lasagna noodles": 12,
        "ground beef": 1,
        "onion": 1,
        "garlic": 2,
        "tomato sauce": 2,
        "water": 2,
        "sugar": 2,
        "dried basil": 1,
        "salt": 1,
        "ricotta cheese": 2,
        "mozzarella cheese": 2,
        "parmesan cheese": 0.5
    },
    "pancakes": {
        "flour": 1,
        "baking powder": 2,
        "sugar": 1,
        "salt": 0.5,
        "milk": 1,
        "egg": 1,
        "butter": 2
    }
}

# Prompt the user for the recipe they want to make and the number of people they are cooking for
recipe_name = input("Enter the name of the recipe you want to make: ").lower()
num_people = int(input("Enter the number of people you are cooking for: "))

# Calculate the new ingredient amounts based on the number of people
recipe = recipes[recipe_name]
new_recipe = {}
for ingredient, amount in recipe.items():
    new_recipe[ingredient] = amount * num_people

# Output the new ingredient amounts to the user
print(f"\nNew ingredient amounts for {recipe_name.title()} for {num_people} people:")
for ingredient, amount in new_recipe.items():
    print(f"{ingredient}: {amount}", "grams")    

