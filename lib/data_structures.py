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

def get_names(spicy_foods):
    spicy_food_names = [name["name"] for name in spicy_foods if name["heat_level"] > 0]
    return spicy_food_names

def get_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
    spicy_food_emoji = [f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶'}" for food in spicy_foods ]
    for spice in spicy_food_emoji:
        print(spice)
    return spicy_food_emoji

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food_name = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return spicy_food_name[0]

def print_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food["heat_level"] > 5]
    print_spicy_foods(spiciest_food)

def get_average_heat_level(spicy_foods):
    total_heat = 0
    spicy_foods_heat_levels = [food["heat_level"] for food in spicy_foods]
    for heat in spicy_foods_heat_levels:
        total_heat += heat
    total_food_length = len(spicy_foods_heat_levels)
    return total_heat / total_food_length


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
)