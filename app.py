import requests
import sys
from flask import Flask, request, render_template
app = Flask(__name__)



def createList(items):
    length = input("How many items are in your fridge? ")
    i = 0
    while i < length:
        items.append(raw_input("Enter item: "))
        i = i + 1

@app.route('/', methods=['GET'])

def searchList(items):
    list = []
    str = ",".join(items)
    print(str)
    recipe_list = []
    app_id = "ae8f41f7"
    app_key = "f6a79be567cb14862a2e7a4f3b4bf17c"

    auth = {'app_id': app_id,
               'app_key': app_key}
    list=auth
    r = requests.get("https://api.edamam.com/search?q=" + str, list)
    status = r.json()
    recipes = status["hits"]
    for recipe in recipes:
       recipe_list.append({"name": recipe["recipe"]["label"], "ingredients": recipe["recipe"]["ingredientLines"],
        "url": recipe["recipe"]["url"]})


    print recipe_list

list = []
createList(list)
(searchList(list))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
