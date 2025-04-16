#  1. Escreva uma expressão regular que procure a palavra Dutch em The Zen of Python.

grep Dutch zen.txt


# 2. Crie uma expressão regular que encontre todos os dígitos da string "
# Arizona 479, 501, 870. California 209, 213, 650".

echo Arizona 479, 501, 870. California 209, 213, 650 | grep [[:digit:]]


#  3. Crie uma expressão regular que encontre qualquer palavra que comece com
# qualquer caractere e seja seguida de duas letras “o”. Em seguida, use o 
# módulo re do Python para encontrar boo e loo na frase
# "The ghost that says boo haunts the loo".

import re

match = re.findall(".oo", "The ghost that says boo haunts the loo")
print(match)

