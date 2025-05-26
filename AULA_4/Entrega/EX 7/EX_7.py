# Lê o número do usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Inicializa o fatorial com 1
fatorial = 1

# Calcula o fatorial apenas se o número for não-negativo
if numero < 0:
    print("Fatorial não definido para números negativos.")
else:
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")
