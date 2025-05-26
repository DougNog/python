# Inicializa a variável
numero = 1

# Cria uma lista para armazenar os números pares
numeros_pares = []

# Loop enquanto o número for menor ou igual a 100
while numero <= 100:
    # Verifica se o número é par
    if numero % 2 == 0:
        numeros_pares.append(numero)
    # Incrementa o número
    numero += 1

# Exibe os números pares
print(numeros_pares)
