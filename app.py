import requests
import sys
from flask import Flask, request, render_template
app = Flask(__name__)
items=[]



def createList():
    length = input("How many items are in your fridge? ")
    i = 0
    while i < length:
        items.append(raw_input("Enter item: "))
        i = i + 1

@app.route('/', methods=['GET'])

def searchList():
    str = ",".join(items)
    recipe_list = []
    app_id = "ae8f41f7"
    app_key = "f6a79be567cb14862a2e7a4f3b4bf17c"
    auth = {'app_id': app_id,
               'app_key': app_key, 'q': str}
    r = requests.get("https://api.edamam.com/search", params=auth)
    status = r.json()
    recipes = status["hits"]
    for recipe in recipes:
        name = recipe["recipe"]["label"]
        url = recipe["recipe"]["url"]
        #ingredients = recipe["recipe"]["ingredientLines"]
        recipe_list.append(name)
    recipeStr = ', '.join(recipe_list)
    return recipeStr

createList()
searchList()

if __name__ == "__main__":
    app.debug = True
    app.run()

