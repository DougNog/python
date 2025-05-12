# salário atual
salario_atual = float(input("Digite o salário atual: "))

# percentual de aumento
percentual_aumento = float(input("Digite o percentual de aumento: "))

# cálculo do aumento
aumento = salario_atual * (percentual_aumento / 100)

# novo salário
novo_salario = salario_atual + aumento

# exibindo o resultado
print(f"Salário atual: R$ {salario_atual:.2f}")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")