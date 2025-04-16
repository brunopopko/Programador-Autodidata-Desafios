# 1. Escreva uma função que receba um número como entrada e retorne esse número
# ao quadrado.

def quadrado(x):
""" Takes an int and returns it multiplied by 2.
:param x: int.
:return: x multiplied by 2.
"""
    return x ** 2

print(quadrado(2))


# 2. Crie uma função que receba uma string como parâmetro e a exiba.


def texto(nome):
""" Imprime a string passada.
:param nome: str.
"""
    print(nome)

texto("Bruno")


# 3. Escreva uma função que receba três parâmetros obrigatórios e dois parâmetros
# opcionais.


def add_mult(x, y, z, a=100, b=1000):
""" Returns the result of two optional params multiplied by the addition of 3 required params.
:param x: int.
:param y: int.
:param z: int.
:param a: int.
:param b: int.
:return: int.
"""
    return x + y + z * a * b

result = add_mult(10, 15, 25)
print(result)


# 4. Escreva um programa com duas funções. A primeira função deve receber um
# inteiro como parâmetro e retornar o resultado do inteiro dividido por 2. A segunda
# função deve receber um inteiro como parâmetro e retornar o resultado do inteiro
# multiplicado por 4. Chame a primeira função, salve o resultado como uma variável
# e passe-a como parâmetro para a segunda função.

def divisao(a):
""" Takes an int and returns it divided by 2.
:param a: int.
:return: int.
"""
    return a / 2

def multiplicacao(b):
""" Takes an int and returns it multiplied by 4.
:param b: int.
:return: int.
"""
    return b * 4

result_divisao = divisao(4)
result_multiplicacao = multiplicacao(result_divisao)

print(result_multiplicacao)


#  5. Escreva uma função que converta uma string em um float e retorne o resultado.
# Use a manipulação de exceções para capturar a exceção que pode ocorrer.

def convert(string):
"""Converts passed in str to int.
:param string = str.
:return: string converted to int.
"""
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float")
        
c = convert("55.0")
print(c)



# 6. Adicione uma docstring a todas as funções que escreveu nos desafios 1-5.
