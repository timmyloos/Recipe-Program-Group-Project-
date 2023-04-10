# Libraries
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

# Data variable
data = json.load(open("recipes.json"))

# List of keys
keys = data.keys()

def get_recipe(word):
    word = word.title()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, keys)) > 0:
        response = input ("Did you mean %s? Enter Y for yes, N for No" % get_close_matches (word, data.keys [0]))
    response.upper()
    if response == "Y":
        return data [get_close_matches(word, data.keys()) [0]]
    elif response == "N":
        return "Sorry we cant find your item today."
    else:
        return "unkown recipe, please try again."

food_item = input ("What do you want to eat?")

print(get_recipe(food_item))