# define the Knight class
class Knight:
  def __init__(self, name, health, attack_power):
    self.name = name
    self.health = health
    self.attack_power = attack_power
  
  def attack(self, opponent):
    print(f"{self.name} attacks {opponent.name}!")
    opponent.health -= self.attack_power
    print(f"{opponent.name}'s health is now {opponent.health}.")

# define the Goblin class
class Goblin:
  def __init__(self, name, health, attack_power):
    self.name = name
    self.health = health
    self.attack_power = attack_power
  
  def attack(self, opponent):
    print(f"{self.name} attacks {opponent.name}!")
    opponent.health -= self.attack_power
    print(f"{opponent.name}'s health is now {opponent.health}.")

# create a Knight object
knight = Knight("Sir Arthur", 100, 10)

# create a Goblin object
goblin = Goblin("Goblin", 50, 5)

# have the Knight and Goblin fight until one of them dies
while True:
  knight.attack(goblin)
  if goblin.health <= 0:
    print(f"{goblin.name} has been defeated!")
    break
  goblin.attack(knight)
  if knight.health <= 0:
    print(f"{knight.name} has been defeated!")
    break
