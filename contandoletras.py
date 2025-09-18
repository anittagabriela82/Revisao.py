vogais= "aeiou"
nvogais=0
nconsoantes=0

frase = input("Digite uma frase:").lower()
for letra in frase:
    if letra.isalpha():
     if letra in vogais:
        nvogais+=1
     else:
       nconsoantes += 1
print(f"\nTotal de vogais: {nvogais}")
print(f"Total de consoantes: {nconsoantes}")