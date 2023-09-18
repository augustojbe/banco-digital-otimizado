# e um conjunto não ordenado, de chave e valores
# são delimitados por chaves. e chaves são imultaveis mas seus valores são mutaveis.
# ao copiar um dicionario vc acaba criando um novo dicionario, vc usa ele quando vc não quer alterar um dado do dicionario original.

pessoa = {"nome": "Augusto", "idade": 35 }

pessoa1 = dict(nome= "Augusto", idade= 35)

print(pessoa,"\n", pessoa1)

pessoa["telefone"] = "3333-1234"

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

for ps in pessoa:
    print(ps, "=", pessoa[ps])
print()
carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
print(carro.get("motor"))