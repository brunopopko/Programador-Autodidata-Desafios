#  1. Crie uma lista de seus músicos favoritos.

musicos = ["Gabriel Expresso", "Bailaço", "Pity"]


# 2. Crie uma lista de tuplas, com cada tupla, contendo a longitude e a latitude de
# algum lugar onde você morou ou que visitou.

localização = [(40.7128, 74.0059), (21.1899, 24.1896)]


# 3. Crie um dicionário contendo diferentes atributos sobre você: altura, cor favorita,
# autor favorito etc.

atributos = {
            "altura": "1,77",
            "peso": "88kg",
            "cor dos olhos": "verde"
}


#4. Escreva um programa que permita que o usuário pergunte sua altura, cor favorita
# ou autor favorito e retorne o resultado a partir do dicionário criado no desafio
# anterior.

atributos = {
            "altura": "1,77",
            "peso": "88kg",
            "cor dos olhos": "verde"
}

pergunta = input("Digite o dado que quer saber: altura, peso ou cor dos olhos.")
                 
if pergunta in atributos:
    resposta = atributos[pergunta]
    print(resposta)


#  5. Crie um dicionário que mapeie seus músicos favoritos para uma lista das canções
# que você mais gosta deles.

cancoes_favoritas = {"Gabriel Expresso": "Tô Sofrendo",
                     "Bailaço": "Troca de Tiro",
                     "Alpha Blondy": "Coco the Rasta"
}


# 6. As listas, as tuplas e os dicionários são apenas alguns dos contêineres internos do
# Python. Faça uma pesquisa sobre os conjuntos (um tipo de contêiner) do Python.
# Quando você usaria um conjunto?

# Resposta: Um uso comum de conjuntos em Python é a computação de operações matemáticas padrão, como união, interseção, diferença e diferença simétrica.
