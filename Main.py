import random

# make a dictionary and add a secret item and each item will have a hint
secrets = {
   "apple": ["food", "fruit", "red or green"],
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
   "tv": ["electronics", "movies", "remote"],

   "school": ["place", "learning", "classes"],
   "park": ["place", "outdoors", "trees"],
   "store": ["place", "buy things", "money"]
}

# another dictionary people can add to
community_secrets = {
   "soccer": ["sport", "ball", "goal"],
   "guitar": ["instrument", "strings", "music"]
}

# merge the second dictionary into the main secrets dictionary
secrets.update(community_secrets)

# choose a secret item
secret_item, secret_hints = random.choice(list(secrets.items()))

# Start at the first hint
hints_used = 0
current_hints = secret_hints
game_running = True

# keep the game running
while game_running:
   
# menu for the player to start the game
   print("\n Welcome to the Guessing Game! Try to guess the secret item.\n ")
   print(input("You can ask for hints by typing '?' at the end of your input. (Enter to continue)"))


   # ask the player to guess or ask a question
   prompt = input("\n Type a guess or ask a hint('?'): ").strip().lower()
   
   # check if the guess is correct
   if prompt == secret_item:
       print("You got it right! You win!")
       break  # game ends

   # check if the player asked for a hint
   if prompt.endswith('?'):
       if hints_used < len(secret_hints):
           print("Answer (as a hint):", secret_hints[hints_used])
           hints_used += 1
       else:
           print("No more hints. The answer was", secret_item)
           play_again = input("Play again? (yes/no)").strip().lower()
           if play_again == "yes":
               secret_item, secret_hints = random.choice(list(secrets.items()))
               current_hints = secret_hints
               hints_used = 0
           else:
               game_running = False
   else:
       # if they typed something wrong that's not '?'
       print("Wrong guess. Try again.")