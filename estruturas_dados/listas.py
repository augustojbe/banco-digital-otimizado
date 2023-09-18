frutas = ["Laranja", "maca", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [5, 6, "C"]
]
#print(letras)
#print(letras[2:])
#print(letras[:2])
#print(letras[1:3])
#print(letras[0:3:2])

carros = ["gol", "celta", "paio"]

#for carro in carros:
#    print(carro)

#for ind, carro in enumerate(carros):
#    print(f"{ind}: {carro}")

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero %2 == 0]
print(pares)
# Elevar ao Quadrado
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)
#print(quadrado.pop())
quadrado.reverse()

print(quadrado)

quadrado.sort()

print(quadrado)

print(len(quadrado))

#for numero in numeros:
#    if numero %2 == 0:
#        pares.append(numero)
#        print(pares)