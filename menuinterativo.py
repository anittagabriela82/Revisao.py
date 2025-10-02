while True:
        print("---Caixa de banco---")
        print("[1] - SALDO")
        print("[2] - FAZER DEPÓSITO")
        print("[3] - FAZER SAQUE")
        print("[4] - SAIR ") 
        escolha = input("Selecione uma opção (ou digite 0 para sair):")
        if escolha.isdigit():
         escolha = int(escolha)
        if escolha ==1:
            print("Opção escolhida foi: SALDO")
        elif escolha == 2:
            print("Opção escolhida foi: DEPÓSITO")
        if escolha == 3:
            print("Opção escolhida foi: SAQUE")
        elif escolha == 0:
             print("finalizando!")
        elif escolha== 4:
            print("SAINDO...")
            break
        else:
            print("Entrada inválida. Digite um número de 1 a 4.")  

        
