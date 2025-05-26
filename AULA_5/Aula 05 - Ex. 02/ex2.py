# Inicializa as variáveis
contador = 0
soma = 0
maior = None
menor = None

# Loop para ler 10 valores inteiros
while contador < 10:
    valor = int(input("Digite um valor inteiro: "))
    
    # Atualiza a soma
    soma += valor
    
    # Verifica o maior valor
    if maior is None or valor > maior:
        maior = valor
    
    # Verifica o menor valor
    if menor is None or valor < menor:
        menor = valor
    
    # Incrementa o contador
    contador += 1

# Calcula a média
media = soma / 10

# Exibe os resultados
print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(f"A média dos números lidos é: {media}")
