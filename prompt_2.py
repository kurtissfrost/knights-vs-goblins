import random

class Character:
  def __init__(self, name, health, attackPower):
    self.name = name
    self.health = health
    self.attackPower = attackPower

  def attack(self, enemy):
    print(f"{self.name} attacks {enemy.name}!")
    enemy.health -= self.attackPower
    print(f"{enemy.name}'s health is now {enemy.health}.")

  def defend(self):
    print(f"{self.name} defends against the enemy attack.")
    self.health += self.health * 0.25
    print(f"{self.name}'s health is now {self.health}.")

  def run(self):
    if random.random() <= 0.5:
      print(f"{self.name} successfully flees from the enemy!")
      return True
    else:
      print(f"{self.name} fails to flee from the enemy!")
      return False

# Create the player character
knight = Character("Knight", 100, 20)

# Create the enemy
goblin = Character("Goblin", 50, 10)

# Start the combat loop
while knight.health > 0 and goblin.health > 0:
  # Display the current health of each character
  print(f"{knight.name}'s health: {knight.health}")
  print(f"{goblin.name}'s health: {goblin.health}")

  # Display the options to the player
  print("What would you like to do?")
  print("1. Attack")
  print("2. Defend")
  print("3. Run")

  # Get the player's input
  choice = int(input("> "))

  # Handle the player's choice
  if choice == 1:
    knight.attack(goblin)
  elif choice == 2:
    knight.defend()
  elif choice == 3:
    if knight.run():
      break
  
  # The goblin attacks or defends at random
  if random.random() <= 0.5:
    goblin.attack(knight)
  else:
    goblin.defend()

# Print a message when the combat
