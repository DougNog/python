# Inicializa as variáveis
contador = 0
soma_temperaturas = 0

print("Digite as temperaturas dos clientes. Para encerrar, digite um valor negativo.")

while True:
    temperatura = float(input("Digite a temperatura do cliente (em °C): "))
    
    # Condição para sair do loop
    if temperatura < 0:
        break
    
    # Classificação da temperatura
    if temperatura < 37.2:
        print("Temperatura normal.")
    elif 37.3 <= temperatura <= 38.0:
        print("Estado febril.")
    elif 38.0 < temperatura <= 39.0:
        print("Com febre.")
    else:  # temperatura > 39.0
        print("Com febre alta.")
    
    contador += 1
    soma_temperaturas += temperatura

# Verifica se pelo menos uma temperatura foi digitada
if contador > 0:
    media = soma_temperaturas / contador
    print(f"\nQuantidade de pessoas analisadas: {contador}")
    print(f"Média das temperaturas: {media:.2f} °C")
else:
    print("Nenhuma temperatura válida foi digitada.")
