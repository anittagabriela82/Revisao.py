soma_total = 0
contador = 0

quantidade = int(input("Digite quantos produtos deseja comprar (ou 0 para encerrar): "))

while contador < quantidade:
    valor = float(input(f"Digite o valor do produto {contador + 1}: "))
    
    if valor < 0:
        print("Valor inválido! Digite um valor positivo.")
        continue  

    soma_total += valor
    contador += 1

print(f"\nA soma total dos produtos é: R$ {soma_total:.2f}")



