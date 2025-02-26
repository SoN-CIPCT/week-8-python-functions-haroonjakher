# Homework Assignment for week 8

def sandwich_ingredients(bread_type, filling, sauce, *veggies):
    #This makes a list of sandwich ingredients
    print(f"This is a sandwhich on {bread_type}, filled with {filling}, with a {sauce} sauce with the following veggies: ")
    for veggie in veggies:
          print(f" - {veggie}")

sandwich_ingredients('sourdough', "prosciutto", "mayo", "tomato", "lettuce")
sandwich_ingredients('whole grain', 'turkey', 'dijon mustard', 'avocado', 'romaine', 'cucumber')