# Classes and Objects Module

The `classes_objects` module showcases the foundational concepts of object-oriented programming in Python. Through this module, you'll understand how to create and interact with classes, leverage inheritance, and utilize polymorphism.

## Files & Descriptions

### 1. `basics.py`
- Fundamental concepts of classes and objects.
    - **`Person` Class**: Represents a basic person with attributes `name` and `age`.
        - `introduce()`: Introduces the person.
        - `celebrate_birthday()`: Celebrates the person's birthday and increases their age.
        - `is_adult(age)`: A static method that checks if a given age is considered adult.

### 2. `inheritance.py`
- Demonstrates the concept of inheritance in OOP.
    - **`Student` Class**: Represents a student and inherits from the `Person` class. Adds an attribute `grade`.
        - `study()`: Method that showcases the student studying for their grade.
    - **`CollegeStudent` Class**: Represents a college student and inherits from the `Student` class. Adds an attribute `major`.
        - `display_major()`: Method that displays the student's major.

### 3. `polymorphism.py`
- Showcases polymorphism, allowing different classes to be treated as instances of the same class.
    - **`Teacher` Class**: Represents a teacher and inherits from the `Person` class. Adds an attribute `subject`.
        - `teach()`: Method that showcases the teacher teaching a subject.
    - **`introduce_person(person)` Function**: Introduces a person regardless of their specific type (`Person`, `Student`, `Teacher`).
    - **`make_person_act(person)` Function**: Makes a person perform an action based on their type.

## Usage

To utilize the classes and functions in this module, you'll first need to import them and then create objects or call functions accordingly. For instance:

```python
from classes_objects.basics import Person
john = Person("John", 25)
john.introduce()  # Outputs: "Hello, my name is John and I am 25 years old."
