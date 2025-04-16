res = ''

while ["s", "n"].count(res.lower()) == 0:
    res = input("Deseja abrir o menu? (S/N): ")
    
if res == "s":
    while True:
        while True:
            print("----Menu----")
            print("Escolha um lanche")
            print("1-Hamburguer")
            print("2-Hotdog")
            print("3-Salgado")
            
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                print("Você escolheu Hamburguer!")
                break
            elif opcao == 2:
                print("Você escolheu Hotdog!")
                break
            elif opcao == 3:
                print("Você escolheu Salgado!")
                break
            else:
                print("Opção invalida")
            
            continuar = input("Deseja incluir mais itens? (s/n)")
                
            if continuar == 'n':
                break
    
print("Programa finalizado.")