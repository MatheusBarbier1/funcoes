def conta_numero(num):
    contador = 1
    while contador <= num:
        contador_str = str(contador)
        print(contador_str * contador)
        contador += 1


num = int(input("Qual o número? "))
conta_numero(num)