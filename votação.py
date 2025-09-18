while True:
    print("---Votação---")
    print("[10] - candidato A")
    print("[20] - candidato B")
    print("[30] - candidato c")
    print("[98] - voto nulo ")
    print("[99] - voto em branco")
    voto= int(input("Escolha uma opção: "))
    if voto == 10:
        print(f"seu voto foi {voto}, Candidato A")
    elif voto == 20:
        print(f"seu voto foi {voto}, Candidato B")
    elif voto == 30:
         print (f"seu voto foi {voto}, Candidato C")
    elif voto == 98:
        print(f"seu voto foi {voto}, NULO")
    elif voto == 99:
            print(f"A opção selecionada foi: {voto}, BRANCO ")
    else:
            print(f"A opção selecionada foi invalida, tente novamente!")


