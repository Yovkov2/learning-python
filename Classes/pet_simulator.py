class Pet:
    def __init__(self, name, animal_type, age):

        self.name = name
        self.animal_type = animal_type
        self.age = age

    def speak(self):

        if self.animal_type.lower() == "dog":
            print(f"{self.name} says: Woof! 🐶")
        elif self.animal_type.lower() == "cat":
            print(f"{self.name} says: Meow! 🐱")
        elif self.animal_type.lower() == "parrot":
            print(f"{self.name} says: Squawk! 🦜")
        else:
            print(f"{self.name} makes an unknown sound 🤔")

    def birthday(self):

        self.age += 1
        print(f"🎂 Happy Birthday, {self.name}! You are now {self.age} years old.")

    def __str__(self):
        return f"{self.name} the {self.animal_type}, {self.age} years old."
class Dog(Pet):
    def __init__(self, name, age, breed):
        """
        Initialize a Dog object, inheriting from Pet.
        :param name: str - dog's name
        :param age: int - dog's age
        :param breed: str - dog's breed
        """
        super().__init__(name, "Dog", age)
        self.breed = breed

    def fetch(self):
        """
        Print a playful fetching message.
        """
        print(f"{self.name} the {self.breed} runs to fetch the ball! 🎾")

    def speak(self):
        """
        Override the speak() method to make it more specific for dogs.
        """
        print(f"{self.name} barks loudly: Woof! Woof! 🐕")


# Create general pets
cat = Pet("Mittens", "Cat", 3)
parrot = Pet("Polly", "Parrot", 2)

# Create a Dog object
dog = Dog("Buddy", 4, "Golden Retriever")

# Display information and actions
print(cat)
cat.speak()
cat.birthday()

print()
print(parrot)
parrot.speak()

print()
print(dog)
dog.speak()
dog.fetch()
dog.birthday()