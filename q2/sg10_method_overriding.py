class Animal:
  def __init__(self, name): 
    self.name = name

  def name(self):
    return self.name
      
  def make_sound(self):
    pass

  def eat(self):
    pass

class Lion(Animal):
  def make_sound(self, sound):
    return f"{self.name} {sound} loudly!"

  def eat(self):
    return f"{self.name} eats {eat}"

class Elephant(Animal):
  def make_sound(self, sound):
    return f"{self.name} {sound}!"

  def eat(self):
    return f"{self.name} eats {eat}"

class Monkey(Animal):
  def make_sound(self, sound):
    return f"{self.name} {sound}!"

  def eat(self):
    return f"{self.name} eats {eat}"

  lion = Lion("Simba")
  elephant = Elephant("Dumbo")
  monkey = Monkey("George")

  print(lion.make_sound())
  print(lion.feed())
  print("-----")

  print(elephant.make_sound())
  print(elephant.feed())
  print("-----")

  print(monkey.make_sound())
  print(monkey.feed())
  print("-----")

