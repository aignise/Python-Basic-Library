## Inheritance

# The Student class inherits from the Person class
class Student(Person):
    # Constructor for the Student class
    def __init__(self, name, age, grade):
        # Call the constructor of the parent (Person) class
        super().__init__(name, age)
        # 'grade' is an attribute specific to the Student class
        self.grade = grade

    # Method specific to the Student class
    def study(self):
        print(f"{self.name} is studying for grade {self.grade}.")


# Class representing a college student, which is a type of student
class CollegeStudent(Student):
    def __init__(self, name, age, grade, major):
        super().__init__(name, age, grade)
        self.major = major  # New attribute specific to CollegeStudent

    def display_major(self):
        """Display the student's major."""
        print(f"{self.name} is majoring in {self.major}.")




## Polymorphism

# The Teacher class also inherits from the Person class
class Teacher(Person):
    # Constructor for the Teacher class
    def __init__(self, name, age, subject):
        # Call the constructor of the parent (Person) class
        super().__init__(name, age)
        # 'subject' is an attribute specific to the Teacher class
        self.subject = subject

    # Method specific to the Teacher class
    def teach(self):
        print(f"{self.name} teaches {self.subject}.")

# This function demonstrates polymorphism; it can accept any object of type Person, Student, or Teacher
def introduce_person(person):
    # Calls the 'introduce' method, irrespective of whether the object is a Person, Student, or Teacher
    person.introduce()


# ... [existing code]

# Function to make a person perform an action based on their type
def make_person_act(person):
    """Make the person perform an action based on their type."""
    if isinstance(person, Teacher):
        person.teach()
    elif isinstance(person, Student):
        person.study()
    elif isinstance(person, Person):
        person.introduce()
    else:
        print("Unknown person type!")

