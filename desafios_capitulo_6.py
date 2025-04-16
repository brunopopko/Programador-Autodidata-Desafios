 # 1. Exiba cada caractere da string “Camus”.
author = "Camus"

print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])


# 2. Escreva um programa que colete duas strings com um usuário, insira-as na string
# "Yesterday I wrote a [resposta_um]. I sent it to [resposta_dois]!"
# e exiba uma nova string.

resposta_um = input("What did you write yesterday?")
resposta_dois = input("Where did you go yesterday?")

new_string = "Yesterday I wrote a {}. I sent it to {}!".format(resposta_um, resposta_dois)

print(new_string)


# 3. Use um método para tornar a string "aldous Huxley was born in 1894."
# gramaticalmente correta fazendo com que a primeira letra da frase seja maiúscula.

x = "aldous Huxley was born in 1894. he was born in the United Kingdom.".title()
print(x)


#  4. Pegue a string "Where now? Who now? When now?" e chame um método que retorne uma lista com esta aparência: 
# ["Where now?", "Who now?", "When now?"] .

lst = "Where now? Who now? When now?".split("?")
print(lst)


#  5. Pegue a lista ["The", "fox", "jumped", "over", "the", "fence", "."] e transforme-a em uma string gramaticalmente correta. É preciso que haja um
# espaço entre cada palavra, mas nenhum espaço entre a palavra fence e o ponto que vem depois dela. (Não se esqueça de que você conheceu um método que
# transforma uma lista de strings em uma única string).

fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)


# 6. Substitua cada ocorrência de "s" em "A screaming comes across the sky." por um cifrão.

s = "A screaming comes across the sky."
s = s.replace("s", "$")
print(s)


#  7. Use um método para encontrar o primeiro índice do caractere "m" na string "Hemingway" .


first_index = "Hemingway".index("m")
print(first_index)


#  8. Encontre um diálogo em seu livro favorito (contendo aspas) e transforme-o em uma string.

quote1 = "'Drink up,' said Ford, 'you've got three pints to get through.'"
quote2 = "'I forgot,' Lennie said softly. 'I tried not to forget. Honest to God I did, George.'"
quote3 = "'Yes,' I said, 'I have a reason,' and added very softly, 'My God.'"
print(quote1 + quote2 + quote3)


#  9. Crie a string "three three three" usando a concatenação e, em seguida, crie-a novamente usando a multiplicação.

concat = "three " + "three " + "three"
mult = "three " * 3
print(concat)
print(mult)


#  10. Fatie a string "It was a bright cold day in April, and the clocks were striking thirteen."
# para que só inclua os caracteres existentes antes da vírgula.

sentence = "It was a bright cold day in Abril, and the clocks were striking thirteen."
slce = sentence[0:33]
print(slce)
