
def matematica():
    a = float(input("Qual o primeiro número? "))
    b = float(input("Qual o segundo número? "))
    escolha = input("Oque você quer fazer? (+ ,- ,/ ,* ) ")


    if escolha == "+":
        soma(a, b)


    elif escolha == "-":
        subtracao(a, b)


    elif escolha == "/":
        divisao(a, b)


    elif escolha == "*":
        multiplicacao(a, b)

    else:
        erro()

def soma(a, b):
    soma = a + b
    print(soma)


def subtracao(a, b):
    subtracao = a - b
    print(subtracao)


def divisao(a, b):
    divisao = a / b
    print(divisao)


def multiplicacao(a, b):
    multiplicacao = a * b
    print(multiplicacao)


def erro():
    print("operação inválida")

matematica()