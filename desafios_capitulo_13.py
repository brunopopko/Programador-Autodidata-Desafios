# 1. Crie as classes Rectangle e Square com um método chamado
# calculate_perimeter que calcule o perímetro das formas que elas representam.
# Crie objetos Rectangle e Square e chame o método em ambos.


class Rectangle():
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calculate_perimeter(self):
        return self.comprimento * 2 + self.largura * 2
    

class Square():
    def __init__(self, lado1):
        self.lado1 = lado1

    def calculate_perimeter(self):
        return self.lado1 * 4


retangulo = Rectangle(25, 50)
quadrado = Square(20)

print(retangulo.calculate_perimeter())
print(quadrado.calculate_perimeter())


#  2. Defina um método em sua classe Square chamado change_size que permita
# passar um número e aumente ou diminua (se o número for negativo) cada lado de
# um objeto Square de acordo com esse número.

class Square():
    def __init__(self, lado1):
        self.lado1 = lado1

    def calculate_perimeter(self):
        return self.lado1 * 4

    def change_size(self, numero):
        self.lado1 += numero

quadrado = Square(100)
print(quadrado.lado1)

quadrado.change_size(200)
print(quadrado.lado1)


#  3. Crie uma classe chamada Shape. Defina um método nela chamado 
#what_am_i que exiba "I am a shape" quando chamado. Altere suas classes 
#Square e Rectangle dos desafios anteriores para que herdem de Shape, crie objetos 
#Square e Rectangle e chame o novo método em ambos.

class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calculate_perimeter(self):
        return self.comprimento * 2 + self.largura *2

class Square(Shape):
    def __init__(self, lado1):
        self.lado1 = lado1

    def calculate_perimeter(self):
        return self.lado1 * 4

retangulo = Rectangle(20, 50)
quadrado = Square(29)

retangulo.what_am_i()
quadrado.what_am_i()


#  4. Crie uma classe chamada Horse e uma classe chamada Rider.
# Use a composição para modelar um cavalo (horse) que tenha um cavaleiro (rider).

class Rider():
    def __init__(self, nome):
        self.nome = nome

class Horse():
    def __init__(self, nome, cavaleiro):
        self.nome = nome
        self.cavaleiro = cavaleiro


cavaleiro = Rider("Bruno")
cavalo = Horse("Foguinho", cavaleiro)

print("The name of Horse is {}".format(cavalo.nome))
print("The name of Rider is {}".format(cavalo.cavaleiro.nome))
