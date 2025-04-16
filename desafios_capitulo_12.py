# 1. Defina uma classe chamada Apple com quatro variáveis de instância para
# representar quatro atributos de uma maçã.

class Aple():
    def __init__(self, peso, cor, gosto, formato):
        self.peso = peso
        self.cor = cor
        self.gosto = gosto
        self.formato = formato


#  2. Crie uma classe Circle com um método chamado area que calcule e retorne sua
# área. Em seguida, crie um objeto Circle, chame area nele e exiba o resultado.
# Use a função pi do módulo interno math do Python.

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi

a_circle = Circle(4)
print(a_circle.calculate_area())


# 3. Crie uma classe Triangle com um método chamado area que calcule e retorne
# sua área. Em seguida, crie um objeto Triangle, chame area nele e exiba o resultado.

class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.height * self.base/2

triangulo = Triangle(20, 30)
print (triangulo.area())


#  4. Crie uma classe Hexagon com um método chamado calculate_perimeter
# que calcule e retorne seu perímetro. Em seguida, crie um objeto 
# Hexagon, chame calculate_perimeter nele e exiba o resultado.

class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

a_hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(a_hexagon.calculate_perimeter())
