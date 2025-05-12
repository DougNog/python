valor = float(input("Digite o valor da prestação: R$ "))
taxa = float(input("Digite a taxa de juros: (%a.m) "))
tempo = int(input("Digite o tempo: (meses) "))

prestacao = valor * (1 + taxa / 100) ** tempo
print(f"Valor da prestação: R$ {prestacao:.2f}")