# Inicializa as variáveis
soma_idade_homens = 0
soma_idade_mulheres = 0
contador_homens = 0
contador_mulheres = 0
contador_total = 0

print("Digite a idade e o sexo de N pessoas.")
print("Para encerrar, digite uma idade negativa.")

while True:
    idade = int(input("Digite a idade: "))
    
    # Condição para sair do loop
    if idade < 0:
        break
    
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().upper()
    
    # Verifica o sexo e atualiza as somas e contadores
    if sexo == 'M':
        soma_idade_homens += idade
        contador_homens += 1
    elif sexo == 'F':
        soma_idade_mulheres += idade
        contador_mulheres += 1
    
    # Incrementa o contador total
    contador_total += 1

# Cálculo das médias
if contador_homens > 0:
    media_homens = soma_idade_homens / contador_homens
else:
    media_homens = 0

if contador_mulheres > 0:
    media_mulheres = soma_idade_mulheres / contador_mulheres
else:
    media_mulheres = 0

if contador_total > 0:
    media_total = (soma_idade_homens + soma_idade_mulheres) / contador_total
else:
    media_total = 0

# Exibe os resultados
print(f"\nIdade média das mulheres: {media_mulheres:.2f} anos")
print(f"Idade média dos homens: {media_homens:.2f} anos")
print(f"Idade média do grupo: {media_total:.2f} anos")
