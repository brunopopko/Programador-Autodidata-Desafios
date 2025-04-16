# 1. Adicione uma variável de classe square_list a uma classe chamada Square para
# que, sempre que você criar um novo objeto Square, ele seja adicionado à lista.

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")


a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)


#  2. Altere a classe Square para que, quando você exibir um objeto Square, uma
# mensagem seja exibida informando o comprimento de cada um dos quatro lados
# da forma. Por exemplo, se você criar um quadrado com Square(29)
# e exibi-lo, o Python deve exibir 29 by 29 by 29 by 29.

class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
print(a_square)


#  3. Escreva uma função que receba dois objetos como parâmetros e retorne True
# se eles forem o mesmo objeto e False se não forem.

def the_same(obj1, obj2):
    return obj1 is obj2

print(the_same(10, 10))
