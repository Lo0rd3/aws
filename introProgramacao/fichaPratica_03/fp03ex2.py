
for _ in range(100):
    print("Menu de opções:\n1.Criar\n2.Atualizar\n3.Eliminar\n4.Sair")
    
    menu=input("por favor escolha uma opção:")

    if menu == "1":
        print("Opção selecionada 1-Criar")
    elif menu == "2":
        print("Opção selecionada 2.Atualizar")
    elif menu == "3":
        print("Opção selecionada 3.Eliminar")
    elif menu == "4":
        print("Opção selecionada 4.Sair")
        break
    else:
        print("Opção invalida por favor um numero inteiro entre 1 e 4")
