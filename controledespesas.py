despesas = []
while True:
    valores = float(input("Registre suas despesas:"))
    if valores == 0:
        break
    if valores > 0:
        despesas.append(valores)
    else:
        print("Digite um valor positivo ou 0 para sair.")
total = sum(despesas)
quantidade = len(despesas)
media = total / quantidade if quantidade > 0 else 0
print("\n--- RESUMO DAS DESPESAS ---")
print(f"1. Total gasto: R$ {total:.2f}")
print(f"2. Número de despesas registradas: {quantidade}")
print(f"3. Valor médio por despesa: R$ {media:.2f}")