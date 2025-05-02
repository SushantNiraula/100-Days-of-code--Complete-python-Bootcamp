"""
On Day 15, while building a coffee machine, we faced several problems such as managing relationships,
handling changes in data, and keeping track of resources.

We were initially using functional or procedural programming, which was not scalable or maintainable.
As the complexity and the interdependence between functions and data structures increased,
we transitioned to Object-Oriented Programming (OOP).

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and their interactions
to design applications and computer programs. OOP allows us to create reusable code and manage complexity
by breaking down a program into smaller, more manageable pieces.

Key Concepts of OOP:
- Classes: Blueprints for creating objects, defining their attributes and methods.
- Objects: Instances of classes that can have unique attributes and methods.
- Attributes: Variables that store data about an object.
- Methods: Functions that define the behavior of an object.

OOP Advantages:
- **Encapsulation**: Encapsulates data and behavior within objects, preventing unintended changes.
- **Inheritance**: Enables child classes to inherit attributes and methods from parent classes, reducing code duplication.
- **Polymorphism**: Allows the use of the same interface for different types of objects, enhancing flexibility.
- **Abstraction**: Hides implementation details and exposes only the relevant behavior of an object.
- **Composition**: Builds complex objects by combining simpler ones.

By adopting OOP, we can write code that is more efficient, maintainable, and scalable.
"""
# Example waiter has attributes like tables, holding_plates and methods like take_order, serve_order, and clean_tables.
from turtle import Turtle, Screen

timmy=Turtle()
timmy.shape('turtle')
timmy.color('coral1')
for i in range(200):
    timmy.forward(1)
my_screen=Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)
my_screen.exitonclick()
