# 1. Exiba cada item da lista a seguir: ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"].

list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for i in list:
    print(i)


# 2. Exiba todos os números de 25 a 50.

for numbers in range(25, 51):
    print(numbers)


#  3. Exiba cada item da lista do primeiro desafio e seus índices.

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, show in enumerate(shows):
    print(index)
    print(show)


#  4. Escreva um programa com um loop infinito (com a opção de digitar q para sair) e
# uma lista de números. A cada iteração do loop, peça ao usuário para fornecer um
# número da lista e informe se o seu palpite estava ou não correto.


numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit!")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")


# 5. Multiplique todos os números da lista [8, 19, 148, 4] por todos os números
# da lista [9, 1, 33, 83] e acrescente cada resultado a uma terceira lista.

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(i * j)

print(list3)
