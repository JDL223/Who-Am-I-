import random

# make a dictionary annd add a secret item and each item will have a hint

secrets_items = {
    "apple": ["food", "fruit" , "red or green"],
    "pizza": ["food", "hot", "cheesy"],
    "burger": ["food", "meat", "bun"],

    "dog": ["animal", "pet", "barks"],
    "cat": ["animal", "pet", "meows"],
    "bird": ["animal", "has wings", "flies"],

    "car": ["vehicle", "has wheels", "drives"],
    "bike": ["vehicle", "two wheels", "pedals"],
    "boat": ["vehicle", "on water", "sails"],

    "phone": ["electronics", "calls", "screens"],
    "computer": ["electronics", "types", "keyboard"],
    "tv": [ "electronics", "movies", "remote"],

    "school" : ["place", "learning", "classes"],
    "park" : ["place", "outdoors", "trees"],
    "store" : ["place", "buy things", "money"]
}

# choose a secret item
secrets_items = random.choice(list(secrets_items.items()))

# Start at the first hint
hints_used = 0
current_hints = secrets_items[1]

#keep the game running
while True:
    # show a hint
    print("Hint:", current_hints[hints_used])