criancas = 0
adolescentes = 0
adultos = 0
idosos = 0
idades = []
while True:
    idade = int(input("Digite a idade (ou 0 para sair): "))
    if idade == 0:
        break
    if idade < 12:
        print("Criança")
        criancas += 1
    elif 13 <= idade <= 17:
        print("Adolescente")
        adolescentes += 1
    elif 18 <= idade <= 59:
        print("Adulto")
        adultos += 1
    elif idade >= 60:
        print("Idoso")
        idosos += 1
    else:
        print("Idade inválida.")
print("\n--- CLASSIFICAÇÃO FINAL ---")
print(f"Crianças: {criancas}")
print(f"Adolescentes: {adolescentes}")
print(f"Adultos: {adultos}")
print(f"Idosos: {idosos}")

