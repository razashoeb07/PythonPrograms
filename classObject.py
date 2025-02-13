class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"the {self.species} make a {self.sound} sound.")


# Creating instances of the Animal class
lion = Animal("lion", "roar")
dog = Animal("dog", "bark")
cat = Animal("cat", "meow")

# Using the instances

lion.make_sound()
dog.make_sound()
cat.make_sound()
