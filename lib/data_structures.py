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
    return [food["name"] for food in spicy_foods]
names_list = get_names(spicy_foods)
print(names_list)

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
spiciest_foods_list = get_spiciest_foods(spicy_foods)
print(spiciest_foods_list)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, target_cuisine):
    for food in spicy_foods:
        if food["cuisine"] == target_cuisine:
            return food
    return None 
target_cuisine = "American"
result = get_spicy_food_by_cuisine(spicy_foods, target_cuisine)

if result:
    print(f"Spicy food from {target_cuisine}: {result['name']} | Heat Level: {'🌶' * result['heat_level']}")
else:
    print(f"No spicy food found for {target_cuisine}.")




def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

print_spiciest_foods(spicy_foods)

def average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)

    if num_spicy_foods == 0:
        return 0 
    return total_heat_level // num_spicy_foods 
average_heat = average_heat_level(spicy_foods)
print(f"Average Heat Level: {average_heat}")

def create_spicy_food(spicy_foods, spicy_food):
    pass
