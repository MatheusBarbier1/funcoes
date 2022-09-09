def dia_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terça"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sabado"
        case _:
            return "Valor {} Inválido".format(dia)

dia = int(input("Qual o dia da semana? "))
print(dia_semana(dia))