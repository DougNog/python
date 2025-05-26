# Inicializa uma lista para armazenar os números
numeros = []

# Loop para verificar os números entre 5 e 100
for numero in range(5, 101):
    # Verifica se o número é divisível por 7 e não é múltiplo de 5
    if numero % 7 == 0 and numero % 5 != 0:
        numeros.append(numero)

# Exibe os números encontrados em sequência
print("Números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5:")
print(numeros)
