#!/usr/bin/env python3
# Define the ingredients and cooking instructions for each recipe
recipes = {
	"pancakes": {
		"ingredients": {
			"flour": {"amount": 1, "unit": "cup(s)"},
			"baking powder": {"amount": 2, "unit": "teaspoon(s)"},
			"sugar": {"amount": 1, "unit": "tablespoon(s)"},
			"salt": {"amount": 0.5, "unit": "teaspoon(s)"},
			"milk": {"amount": 1, "unit": "cup(s)"},
			"egg": {"amount": 1, "unit": ""},
			"butter": {"amount": 2, "unit": "tablespoon(s)"}
		},
		"instructions": [
			"In a medium bowl, whisk together the flour, baking powder, sugar, and salt.",
			"In another bowl, whisk together the milk, egg, and melted butter.",
			"Pour the wet ingredients into the dry ingredients and stir until just combined.",
			"Heat a large nonstick skillet over medium-high heat.",
			"Ladle the batter onto the skillet, using about 1/4 cup for each pancake.",
			"Cook until the edges are set and bubbles form on the surface, about 2 minutes.",
			"Flip the pancakes and cook until the other side is golden brown, about 1 to 2 minutes more."
		]
	},
	"chocolate cake": {
		"ingredients":{
			"flour": {"amount": 2, "unit": "cup(s)"},
			"sugar": {"amount": 2, "unit": "cup(s)"},
			"cocoa powder": {"amount": 0.75, "unit": "cup(s)"},
			"baking powder": {"amount": 2, "unit": "teaspoon(s)"},
			"baking soda": {"amount": 1.5, "unit": "teaspoon(s)"},
			"salt": {"amount": 1, "unit": "teaspoon(s)"},
			"milk": {"amount": 1, "unit": "cup(s)"},
			"vegetable oil": {"amount": 0.5, "unit": "cup(s)"},
			"eggs": {"amount": 2, "unit": ""},
			"vanilla extract": {"amount": 2, "unit": "teaspoon(s)"},
			"boiling water": {"amount": 1, "unit": "cup(s)"},
		},
		"instructions": [
			"Preheat oven to 350°F. Grease and flour two 9-inch round baking pans.",
			"In a large mixing bowl, combine the flour, sugar, cocoa powder, baking powder, baking soda, and salt.",
			"Add the milk, vegetable oil, eggs, and vanilla extract to the dry ingredients and mix on medium speed for 2 minutes.",
			"Stir in the boiling water (the batter will be thin).",
			"Pour the batter evenly into the prepared pans.",
			"Bake for 30-35 minutes or until a toothpick inserted in the center comes out clean.",
			"Cool the cakes in the pans for 10 minutes, then remove them from the pans and place them on wire racks to cool completely."
		]
	},
	"chicken alfredo": {
		"ingredients": {
			"spaghetti": {"amount": 4, "unit": "ounce(s)"},
			"chicken breast": {"amount": 0.5, "unit": "pound(s)"},
			"olive oil": {"amount": 1, "unit": "tablespoon(s)"},
			"garlic": {"amount": 1, "unit": "clove(s)"},
			"heavy cream": {"amount": 1, "unit": "cup(s)"},
			"parmesan cheese": {"amount": 0.25, "unit": "cup(s)"},
			"salt": {"amount": 0.5, "unit": "teaspoon(s)"},
			"pepper": {"amount": 0.5, "unit": "teaspoon(s)"}
		},
		"instructions": [
			"Cook spaghetti according to package instructions.",
			"Season chicken breast with salt and pepper.",
			"In a large pan, heat olive oil over medium-high heat. Add garlic and sauté for 1-2 minutes, until fragrant.",
			"Add chicken breast to the pan and cook until browned and cooked through, about 5-7 minutes per side.",
			"Remove chicken from pan and set aside.",
			"Reduce heat to medium and add heavy cream to the same pan, stirring until it comes to a simmer.",
			"Add parmesan cheese, salt, and pepper to the pan and whisk until the cheese is melted and the sauce is smooth.",
			"Slice the chicken and add it back to the pan, along with the cooked spaghetti.",
			"Stir everything together until the chicken and spaghetti are coated in the sauce.",
			"Serve hot."
		]
	},
	"vegetable stir-fry": {
		"ingredients": {
			"rice": {"amount": 2, "unit": "cup(s)"},
			"soy sauce": {"amount": 1, "unit": "tablespoon(s)"},
			"cornstarch": {"amount": 1, "unit": "teaspoon(s)"},
			"sesame oil": {"amount": 1, "unit": "teaspoon(s)"},
			"garlic": {"amount": 2, "unit": "clove(s)"},
			"ginger": {"amount": 1, "unit": "teaspoon(s)"},
			"carrots": {"amount": 2, "unit": "cup(s)"},
			"broccoli": {"amount": 2, "unit": "cup(s)"},
			"red bell pepper": {"amount": 1, "unit": "cup(s)"},
			"snow peas": {"amount": 1, "unit": "cup(s)"},
			"water chestnuts": {"amount": 1, "unit": "can(s)"},
			"green onions": {"amount": 1, "unit": "cup(s)"}
		},
		"instructions": [
			"Cook the rice according to package instructions.",
			"Mix together the soy sauce, cornstarch, and sesame oil in a small bowl.",
			"Heat a wok or large skillet over high heat.",
			"Add the garlic and ginger and stir-fry for 30 seconds.",
			"Add the carrots and stir-fry for 2 minutes.",
			"Add the broccoli and red bell pepper and stir-fry for 2 minutes.",
			"Add the snow peas and water chestnuts and stir-fry for 1 minute.",
			"Add the green onions and soy sauce mixture and stir-fry for 1 minute or until the sauce has thickened.",
			"Serve the stir-fry over the cooked rice."
		]
	},
	"lasagna": {
		"ingredients": {
			"lasagna noodles": {"amount": 12, "unit": "noodles"},
			"ground beef": {"amount": 1, "unit": "pound(s)"},
			"onion": {"amount": 1, "unit": ""},
			"garlic": {"amount": 2, "unit": "clove(s)"},
			"tomato sauce": {"amount": 2, "unit": "cup(s)"},
			"water": {"amount": 2, "unit": "cup(s)"},
			"sugar": {"amount": 2, "unit": "teaspoon(s)"},
			"dried basil": {"amount": 1, "unit": "teaspoon(s)"},
			"salt": {"amount": 1, "unit": "teaspoon(s)"},
			"ricotta cheese": {"amount": 2, "unit": "cup(s)"},
			"mozzarella cheese": {"amount": 2, "unit": "cup(s)"},
			"parmesan cheese": {"amount": 0.5, "unit": "cup(s)"}
		},
		"instructions": [
			"Cook lasagna noodles according to package directions.",
			"In a large skillet, cook ground beef, onion, and garlic over medium heat until the beef is browned. Drain excess fat.",
			"Add tomato sauce, water, sugar, basil, and salt to the skillet. Bring to a boil, then reduce heat and simmer for 20 minutes.",
			"In a medium bowl, mix together ricotta cheese and 1 cup of mozzarella cheese.",
			"Preheat oven to 375°F. Grease a 9x13 inch baking dish.",
			"To assemble lasagna, spread 1 cup of the meat sauce in the bottom of the prepared baking dish. Layer with 4 lasagna noodles, then spread half of the ricotta cheese mixture over the noodles. Top with 1 cup of the meat sauce, then sprinkle with 1/4 cup of parmesan cheese. Repeat layers, ending with meat sauce and parmesan cheese.",
			"Cover the baking dish with foil and bake in preheated oven for 25 minutes.",
			"Remove foil and bake for an additional 25 minutes.",
			"Remove from oven and let stand for 10 minutes before serving."
		]
	},
}

# Prompt the user for the recipe they want to make and the number of people they are cooking for
recipe_name = input("Enter the name of the recipe you want to make: ").lower()
num_people = int(input("Enter the number of people you are cooking for: "))

# Calculate the new ingredient amounts based on the number of people
recipe = recipes[recipe_name]["ingredients"]
new_recipe = {}
for ingredient, data in recipe.items():
	new_amount = data["amount"] * num_people
	new_recipe[ingredient] = {"amount": new_amount, "unit": data["unit"]}
	
# Output the new ingredient amounts and cooking instructions to the user
print(f"\nNew ingredient amounts for {recipe_name.title()} for {num_people} people:")
for ingredient, data in new_recipe.items():
	print(f"{ingredient}: {data['amount']} {data['unit']}")
print("\nInstructions:")
for step in recipes[recipe_name]["instructions"]:
	print(step)
	