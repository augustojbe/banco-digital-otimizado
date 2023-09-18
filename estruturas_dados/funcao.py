# tornar o codigo mas simples, e reaproveitaveis, assim programamos de madeira estruturada.
# em python tudo e objeto, funções tambem são funções.

def exibir_mensagem():
    print("Ola mundo")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")

#exibir_mensagem()
#exibir_mensagem_2(nome="Augusto")
#exibir_mensagem_2("Esther")
#exibir_mensagem_3()
#exibir_mensagem_3(nome="Fernando")

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-123", marca="Fiate", motor="1.0", combustivel="Gasolina")

def criar_carro_2(*,modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_2(modelo="Palio", ano=2000, placa="ABC-123", marca="Fiate", motor="1.0", combustivel="Gasolina" )


def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

op = somar

print(op(150, 50))

salario = 1200

def salario_bonos(bonos):
    global salario
    salario += bonos
    return salario

novo_salarion = salario_bonos(500)
print(novo_salarion)