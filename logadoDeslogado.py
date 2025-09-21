luz_acesa=False

while True:
    escolha=input("o que fazer?( 1: apertar interruptor, 0: sair): ")
    if escolha.isdigit():
        escolha= int(escolha)
        if escolha == 1:
            print("A luz está ACESA.")
        else:
            print("A luz está APAGADA.")                                                                                                                                 
    elif escolha == 0:
            print("Saindo...")
            break
    else:
            print("Opção inválida. Digite 1 para apertar o interruptor ou 0 para sair.")  
