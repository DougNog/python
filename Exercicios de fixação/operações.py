num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#escolha a operação
print("Escolha a operação que deseja realizar:")
print("1 - Divisão")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Sair")
resul = int(input("Digite a opção desejada: "))

#realiza a operação
if resul == 1:
    print(f"A divisão de {num1} por {num2} é: {num1 / num2:.2f}")
elif resul == 2:
    print(f"A subtração de {num1} por {num2} é: {num1 - num2:.2f}")
elif resul == 3:
    print(f"A multiplicação de {num1} por {num2} é: {num1 * num2:.2f}")
elif resul == 4:
    print("Saindo...")
else:
    print("Opção inválida!")