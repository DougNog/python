# Função para calcular o fatorial
def fatorial(n):
    if n < 0:
        return None  # Fatorial não definido para números negativos
    elif n == 0 or n == 1:
        return 1  # Fatorial de 0 e 1 é 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Recebe um número do usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Calcula o fatorial
resultado_fatorial = fatorial(numero)

# Exibe o resultado
if resultado_fatorial is not None:
    print(f"O fatorial de {numero} é: {resultado_fatorial}")
else:
    print("Fatorial não definido para números negativos.")
