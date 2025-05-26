soma_mulheres = 0
soma_homens = 0
soma_total = 0
cont_mulheres = 0
cont_homens = 0

for i in range(10):
    print(f"\nPessoa {i+1}")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().upper()

    soma_total += idade

    if sexo == 'F':
        soma_mulheres += idade
        cont_mulheres += 1
    elif sexo == 'M':
        soma_homens += idade
        cont_homens += 1
    else:
        print("Sexo inválido. Não será contado.")

# Cálculos das médias com verificação para evitar divisão por zero
media_mulheres = soma_mulheres / cont_mulheres if cont_mulheres > 0 else 0
media_homens = soma_homens / cont_homens if cont_homens > 0 else 0
media_grupo = soma_total / 10

print("\n--- Resultados ---")
print(f"Idade média das mulheres: {media_mulheres:.2f}")
print(f"Idade média dos homens: {media_homens:.2f}")
print(f"Idade média do grupo: {media_grupo:.2f}")
