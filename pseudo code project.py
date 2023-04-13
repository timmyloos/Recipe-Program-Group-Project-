# 1. Define the ingredients for each recipe
# 2. Prompt the user for the recipe they want to make and the number of people they are cooking for
# 3. Calculate the new ingredient amounts based on the number of people
# 4. Output the new ingredient amounts to the user


# Define the ingredients for each recipe
recipes = {
    "recipe_name_1": {
        "ingredient_1": amount_1,
        "ingredient_2": amount_2,
        ...
    },
    "recipe_name_2": {
        "ingredient_1": amount_1,
        "ingredient_2": amount_2,
        ...
    },
    ...
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
    print(f"{ingredient}: {amount}")
