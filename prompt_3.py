import random

# Initialize player and goblin stats
player_hp = 10
player_atk = 3
goblin_hp = 6
goblin_atk = 2

# Start the combat loop
while player_hp > 0 and goblin_hp > 0:
  # Display current health
  print(f"Your health: {player_hp}")
  print(f"Goblin's health: {goblin_hp}")
  
  # Player's turn
  print("What do you want to do?")
  print("1. Attack")
  print("2. Defend")
  print("3. Run")
  choice = int(input())
  
  if choice == 1:
    # Attack the goblin
    print("You attack the goblin!")
    goblin_hp -= player_atk
  elif choice == 2:
    # Defend and reduce damage taken by 25%
    print("You defend and reduce the damage taken by 25%.")
    player_atk = player_atk * 0.75
  elif choice == 3:
    # Try to run away
    print("You try to run away...")
    if random.randint(1, 2) == 1:
      # Success! End the combat
      print("You successfully run away!")
      break
    else:
      # Failure! Stay in combat
      print("You failed to run away!")
      
  # Goblin's turn
  print("The goblin attacks you!")
  action = random.randint(1, 2)
  if action == 1:
    # Attack the player
    player_hp -= goblin_atk
  elif action == 2:
    # Defend and reduce damage taken by 25%
    goblin_atk = goblin_atk * 0.75

# Print the outcome of the combat
if player_hp > 0:
  print("You have defeated the goblin!")
else:
  print("You have been defeated by the goblin.")
