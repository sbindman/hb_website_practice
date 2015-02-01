from random import choice
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    return render_template("compliment.html", user=player)

@app.route('/food')
def food():
    vegetarian = request.args.get("vegetarian")
    selected_food = None
    FOOD = {"veggie" : ["pasta", "veggies and tofu", "eggplant parm", "cheese and crackers"] , "non-veggie" : ["pasta bolognese", "fish in paper", "chicken fried rice", "hamburgers"]}

    if vegetarian == "yes":
        selected_food = choice(FOOD["veggie"])
    else:
        selected_food = choice(FOOD["non-veggie"])


    return render_template("food.html", food=selected_food)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
