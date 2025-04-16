#1. Exiba três strings diferentes.

print("primeira")
print("segunda")
print("terceira")


#2. Escreva um programa que exiba uma mensagem se uma variável for menor do
#que 10 e outra mensagem se a variável for maior ou igual a 10.

numero = 15
if numero < 10:
    print("O número é menor do que 10")
else:
    print("O número é maior ou igual a 10")


#3. Escreva um programa que exiba uma mensagem se uma variável for menor ou
#igual a 10, outra mensagem se a variável for maior do que 10, mas menor ou igual a
#25, e ainda outra mensagem se a variável for maior do que 25.

numero = 17
if numero <= 10:
    print("O número é menor ou igual a 10")
elif numero > 10:
    if numero <= 25:
        print("O número é maior do que 10 e menor do que 25")
elif numero > 25:
    print("O número é maior do que 25")


#4. Crie um programa que divida duas variáveis e exiba o resto.

print(100 % 13)


#5. Crie um programa que receba duas variáveis, as divida, e exiba o quociente.

a = 200
b = 17
print(a // b)


#6. Escreva um programa com uma variável age que receba um inteiro e exiba strings
#diferentes dependendo de que inteiro age receber.

age = 19
maioridade = 18
if age >= 18:
    print("Indivíduo maior de idade")
else:
    print("Indivíduo menor de idade")
