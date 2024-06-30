# polymorphism
# method overiding 

class Shape:
    def area(self):
        pass
    
class Circle(Shape): 
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2 

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
def print_area(shape):
    print('Area:',shape.area())
        
rectangle = Rectangle(5,6)
circle = Circle(5)

print_area(rectangle)
print_area(circle)

# 2
class Animal:
   def speak(self):
     pass

class Dog(Animal):
    def speak(self):
        return 'wooof!!'

class Cat(Animal):
    def speak(self):
        return 'meoww!!'

def make_sound(animal):
    print(animal.speak())

animals = [Dog(),Cat()]
for animal in animals:
    make_sound(animal)
    
# 3
class Employee :
    def __init__(self,name):
        self.name=name 
    def calculate_salary(self):
        pass
    
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000
    
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 25000

employees = [FullTimeEmployee('BOB'),PartTimeEmployee('jenifer')]
for i in employees: 
    print(f"{i.name}'s salary:", i.calculate_salary())