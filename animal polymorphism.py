class Animal:
    def move(self):
        pass  # Base method, to be overridden

class Dog(Animal):
    def move(self):
        print("Dog runs 🐕")

class Bird(Animal):
    def move(self):
        print("Bird flies 🦅")

class Fish(Animal):
    def move(self):
        print("Fish swims 🐟")

# Using polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
