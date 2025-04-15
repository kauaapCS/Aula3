linhas = int(input("Digite a quantidade de linhas: "))

for i in range(linhas):
    for j in range(i + 1):
        print("*", end=" ")
    print()