#  1. Encontre um arquivo em seu computador e exiba seu conteúdo usando o Python.

with open("fav_color.txt", "r") as f:
    print(f.read())


#  2. Escreva um programa que faça uma pergunta a um usuário e salve a resposta em
# um arquivo.

answer = input("What is your favorite color?")
with open("fav_color.txt", "w") as f:
    f.write(answer)


#  3. Pegue os itens desta lista de listas, [["Top Gun", "Risky Business",
# "Minority Report"], ["Titanic", "The Revenant", "Inception"],
# ["Training Day", "Man on Fire", "Flight"]] , e grave-os em um arquivo
# CSV. Os dados de cada lista devem ser uma linha no arquivo, com cada item da
# lista separado por uma vírgula.

import csv


#filmes = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
#with open("filmes.csv", "w") as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=",")
#    for lista_filmes in filmes:
#        spamwriter.writerow(lista_filmes)


with open("filmes.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
