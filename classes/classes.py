# Define the Person class
class Person:
    # The constructor (__init__) initializes the object when created
    def __init__(self, name, age):
        # 'self' refers to the instance being created; 'name' and 'age' are attributes of the class
        self.name = name
        self.age = age

    # Method to introduce the person
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        

    # Method to celebrate the person's birthday
    def celebrate_birthday(self):
        """Increments the person's age by 1."""
        self.age += 1
        print(f"It's {self.name}'s birthday! They are now {self.age} years old.")

    # Static method that doesn't need a class instance to be called
    @staticmethod
    def is_adult(age):
        """Check if a person with the given age is an adult."""
        return age >= 18
