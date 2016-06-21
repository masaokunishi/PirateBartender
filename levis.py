import random

questions = {
    "slim": "do you like tight jeans?",
    "straight": "do you like traditional loooking?",
    "relax": "do you like loose jeans?",
}

models = {
    "slim": ["510", "511", "512"],
    "straight": ["501", "502", "503"],
    "relax": ["550", "551", "552"] 
}

def find_jeans():
    jeans = {}
    for type, question in questions.items():
        print(question)
        jeans[type] = input().lower() in ["y", "yes"]
        print("")
    return jeans

def sell_model(jeans):
    model = []
    for serial_number, liked in jeans.items():
        if not liked:
            continue
        model.append(random.choice(models[serial_number]))
    return model
    
def main():
    jeans = find_jeans()
    model = sell_model(jeans)
    print("one model coming up.")
    print("It's full of good stuff. The jeans is:")
    for jeans_model in model:
        print("A {}".format(jeans_model))

if __name__ == "__main__":
    main()

    