numbers = range(1, 11)

for linha in numbers:
    print("-" * 20)
    for coluna in numbers:
        print(f"{linha} x {coluna} = {linha * coluna}")
print("-" * 20)