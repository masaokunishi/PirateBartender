import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def find_choices():
    choices = {}
    for type, question in questions.items():
        print(question)
        choices[type] = input().lower() in ["y", "yes"]
        print ("")
    return choices
    
def make_drink(choices):
    drink = []
    for ingredient_type, liked in choices.items():
        if not liked:
            continue
        
        drink.append(random.choice(ingredients[ingredient_type]))
    return drink
    
def main():
    choices = find_choices()
    drink = make_drink(choices)
    print("One drink coming up.")
    print("It's full of good stuff. The recepit is:")
    for ingredient in drink:
        print("A {}".format(ingredient))

if __name__ == "__main__":
    main()
    
    