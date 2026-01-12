import random

# make a dictionary annd add a secret item and each item will have a hint

secrets = {
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
secret_name, secret_hints = random.choice(list(secrets.items()))

# Start at the first hint
hints_used = 0
current_hints = secret_hints
game_running = True

# keep the game running
while game_running:
    # ask the player to guess or ask a question
    prompt = input("Type a guess or a hint(?): ").strip().lower()

    # if the player asked a question, give a hint as an answer
    if prompt.endswith('?'):
        if hints_used < len(secret_hints):
            print("Answer (as a hint):", secret_hints[hints_used])
            hints_used += 1
        else:
            print("No more hints. The answer was", secret_name)
            play_again = input("Play again? (yes/no)").strip().lower()
            if play_again == "yes":
                secret_name, secret_hints = random.choice(list(secrets.items()))
                current_hints = secret_hints
                hints_used = 0
            else:
                game_running = False

    else:
        # treat input as a guess
        guess = prompt
        if guess == secret_name:
            print("You got it right!")
            play_again = input("Play again? (yes/no)").strip().lower()
            if play_again == "yes":
                secret_name, secret_hints = random.choice(list(secrets.items()))
                current_hints = secret_hints
                hints_used = 0
            else:
                game_running = False
        else:
            print("Wrong guess...")
            # automatically answer one question for them by giving a hint
            if hints_used < len(secret_hints):
                print("Here's a hint:", secret_hints[hints_used])
                hints_used += 1
            else:
                print("Out of hints. The answer was", secret_name)
                play_again = input("Play again? (yes/no)").strip().lower()
                if play_again == "yes":
                    secret_name, secret_hints = random.choice(list(secrets.items()))
                    current_hints = secret_hints
                    hints_used = 0
                else:
                    game_running = False