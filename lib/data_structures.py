spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_):
    new_list = []
    for food in spicy_:
        new_list.append(food["name"])
    return new_list
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_):
    spiciest_list=[food for food in spicy_ if food["heat_level"]>5]
    return spiciest_list
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_):
    for food in spicy_:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_, cuisine):
    for food in spicy_:
        if food["cuisine"] == cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))


def print_spiciest_foods(spicy_):
    for food in spicy_:
        if food['heat_level']>5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = "🌶" * food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_):
    total_heat_level = sum(food["heat_level"] for food in spicy_)
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0
    else:
        average = total_heat_level / num_foods
        return int(average)
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_list, new_food):
    new_list = spicy_list.copy()  # Make a copy of the original list
    new_list.append(new_food)   # Append the new food to the copy
    return new_list
new_spicy_foods = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}
create_spicy_food(spicy_foods, new_spicy_foods)
