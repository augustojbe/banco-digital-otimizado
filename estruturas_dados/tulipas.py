# Tuplas
# tuplas e um objeto imutavel, ele leva quase todos os metodos da lista,
# porem você nao pode atualizar, ela serve para para quando você que usar algo que seja imutavel.

frutas = ("Laranja", "maca", "uva",)

letras = tuple("python")

print(letras)

pais = ("Brasil")
print(pais)

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (5, 6, "c"),
)

print(matriz)

carros = ("gol")
print(isinstance(carros, tuple))


