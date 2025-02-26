dia = "Terça"

match dia:
    case "Domingo":
        print('Um dia frio, um bom lugar pra ler um livro')
    case "Segunda" | "Terça":
        print("Bleh!")
    case "Sexta":
        print("Sextou")
    case "Sábado":
        print("Dia de cinema")
    case _:
        print("Dia sem graça")