import math
import json
# https://fs1.itstep.org/api/v1/files/SgjnzzaLJPOv1RHACPi6oar0gUF_LP31?inline=true
# Завдання 1
# Створіть базовий клас «Фігура» з методом для підрахунку
# площі. Створіть похідні класи: прямокутник, коло, прямокутний трикутник, трапеція, зі своїми методами для підрахунку
# площі. 
class Figure:
    def __init__(self, figureName):
        self.figureName = figureName
    def find_area(self):
        return f"Area of {self.figureName} = "
class Rectangle(Figure):
    def __init__(self, figureName, a_side, b_side):
        super().__init__(figureName)
        self.a_side = a_side
        self.b_side = b_side
    def find_area(self):
        return super().find_area()+ f"{self.a_side*self.b_side}"
class Circle(Figure):
    def __init__(self, figureName, r):
        super().__init__(figureName)
        self.radius = r
    def find_area(self):#pi*r^2
        return super().find_area() + f"{math.pi*self.radius*self.radius}"
   
class Right_Triangle(Figure):
    def __init__(self, figureName, a,b):
        super().__init__(figureName)
        self.a_katet = a
        self.b_katet = b
    def find_area(self):#1/2a*b
        return super().find_area() + f"{1/2*self.a_katet*self.b_katet}"
class Trapezoid(Figure):
    def __init__(self, figureName, a, b, h):
        super().__init__(figureName)
        self.a_side = a
        self.b_side = b
        self.height = h
    def find_area(self):#(a+b)/2 * h
        return super().find_area() + f"{(self.a_side*self.b_side)*self.height/2}"

def task1():
    figure1 = Rectangle("rectangle",4,5)
    print(figure1.find_area())
    figure2 = Circle("circle", 5)
    print(figure2.find_area())
    figure3 = Right_Triangle("triangle", 4, 8)
    print(figure3.find_area())
    figure4 = Trapezoid("trapezoid", 4, 5, 6)
    print(figure4.find_area())
#task1()
#____________________________________________________________________________
# Завдання 3
# Створіть базовий клас Shape для рисування плоских фігур.
# Визначте методи:
# ■ Show() — виведення на екран інформації про фігуру;
# ■ Save() — збереження фігури у файл;
# ■ Load() — зчитування фігури з файлу.
# Визначте похідні класи:
# ■ Square — квадрат із заданими з координатами лівого
# верхнього кута та довжиною сторони.
# ■ Rectangle — прямокутник із заданими координатами
# верхнього лівого кута та розмірами.
# ■ Circle — коло із заданими координатами центру та радіусом.
# ■ Ellipse — еліпс із заданими координатами верхнього кута
# описаного навколо нього прямокутника зі сторонами,
# паралельними осям координат, та розмірами цього прямокутника.
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну
# фігуру

class Shape():
    def __init__(self, name):
        self.name = name
    
    def show(self):
        return f"\t\tShape Info:\nname: {self.name}"
    
    def save(self, filename):
        data = {
            "class": self.__class__.__name__,
            "info":self.serialize()
        }
        with open(filename, "w") as file:
            json.dump(data,file)
   
    @staticmethod
    def load(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        
        class_name = data["class"]
        info = data["info"]
        
        if class_name == "Square":
            return Square(**info)
        elif class_name == "Rectangle":
            return Rectangle(**info)
        elif class_name == "Circle":
            return Circle(**info)
        elif class_name == "Ellipse":
            return Ellipse(**info)
        else:
            raise ValueError(f"Unknown class: {class_name}")
   
    def serialize(self):
        data = {"name":self.name}
        return data
class Square(Shape):
    def __init__(self, name,x,y,length):
        super().__init__(name)
        self.x = x
        self.y = y
        self.length = length
    def show(self):
        return super().show() + f"\nx = {self.x}\ny = {self.y}\nlength = {self.length}"
    def serialize(self):
        data = super().serialize()
        data.update({"x": self.x, "y": self.y, "length": self.length})
        return data
class Rectangle(Shape):
    def __init__(self, name,x,y,width,height):
        super().__init__(name)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def show(self):
        return super().show() + f"\nx = {self.x}\ny = {self.y}\nwidth = {self.width}\nheight = {self.height}"
    def serialize(self):
        data = super().serialize()
        data.update({"x": self.x, "y": self.y, "width": self.width, "height": self.height})
        return data
class Circle(Shape):
    def __init__(self, name,x,y,radius):
        super().__init__(name)
        self.x = x
        self.y = y
        self.radius = radius
    def show(self):
        return super().show() + f"\nx = {self.x}\ny = {self.y}\nradius = {self.radius}"
    def serialize(self):
        data = super().serialize()
        data.update({"x": self.x, "y": self.y, "radius": self.radius})
        return data
class Ellipse(Shape):
    def __init__(self, name,x,y,width,height):
        super().__init__(name)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def show(self):
        return super().show() + f"\nx = {self.x}\ny = {self.y}\nwidth = {self.width}\nheight = {self.height}"
    def serialize(self):
        data =  super().serialize()
        data.update({"x": self.x, "y": self.y, "width": self.width, "height": self.height})
        return data

shapes = [
    Square("Square", 0, 0, 5),
    Rectangle("Rectangle", 1, 2, 10, 6),
    Circle("circle", 4, 5, 8),
    Ellipse("ellipse", 4,5, 7, 8)
]
for i, shape in enumerate(shapes):
    shape.save(f"shape_{i}.json")

loaded_shapes = []
for i in range(len(shapes)):
    shape = Shape.load(f"shape_{i}.json")
    loaded_shapes.append(shape)

for shape in loaded_shapes:
    print(shape.show())
