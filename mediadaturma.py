alunos=0
soma=0
contador= int(input("Quantos alunos tem na turma: "))
for i in range(contador):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    while nota < 0 or nota > 10:
        print("Erro, tente novamente")
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))  
soma += nota
media = soma/contador
print(f"\nA média da turma é: {media:.2f}")

     
