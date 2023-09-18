# Um set é uma coleção de item que não são repetidos, e usado para representar conjuntos matematicos
# usamos também para eliminar conjuntos duplicados
# para acessar o indice de um conjunto vc precisa transforma-lo em uma lista


numero = set([1, 2, 3, 4, 1, 4])
fruta = set("abacaxi")

#print(numero,"\n",fruta)


linguagem = {"javaScript", "Java", "Python", "Java"}
#print(linguagem)

conjunto_a = {1,2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
print(1 in conjunto_a)
print(10 in conjunto_b)

