alguem_reprovou = False

for i in range(5):
    nota = -1  # valor inválido inicial para entrar no while

    while nota < 0 or nota > 10:
        nota_str = input(f"Digite a nota do aluno {i+1} (0 a 10): ")
        
        if nota_str.replace('.', '', 1).isdigit():  # permite números com ponto
            nota = float(nota_str)
            if nota < 0 or nota > 10:
                print("Nota fora do intervalo! Digite um valor entre 0 e 10.")
        else:
            print("Entrada inválida! Digite um número válido.")

    if nota < 5.0:
        alguem_reprovou = True

if alguem_reprovou:
    print("A turma possui pelo menos um aluno reprovado.")
else:
    print("Parabéns! Todos na turma foram aprovados.")


