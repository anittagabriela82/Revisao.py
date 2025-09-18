N= int(input("Digite um número positivo:"))
fatorial= 1
if N < 0:
    int(input("digite um numero positivo:"))
else:
    for i in range(1, N + 1):
        fatorial *= i
    print(f"O fatorial de {N} é {fatorial}")