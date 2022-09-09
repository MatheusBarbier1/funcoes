def conta():
    conta = float(input("Qual o valor da conta? "))
    print("A gorjeta do garçom deu:",gorjeta(conta))

def gorjeta(conta):
    gorjeta = conta * 0.1
    return gorjeta

conta()
