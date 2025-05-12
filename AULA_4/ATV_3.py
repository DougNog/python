total_temperaturas = 0
soma_temperaturas = 0.0

while True:
    temperatura = float(input("Digite a temperatura (°C) ou um valor negativo para encerrar: "))
    
    if temperatura < 0:
        break

    total_temperaturas += 1
    soma_temperaturas += temperatura

    if temperatura < 37.2:
        print("Temperatura normal.")
    elif 37.2 <= temperatura < 38.0:
        print("Estado febril.")
    elif 38.0 <= temperatura < 39.0:
        print("Febre.")
    else:
        print("Febre alta.")

if total_temperaturas > 0:
    media = soma_temperaturas / total_temperaturas
    print(f"\nTotal de pessoas analisadas: {total_temperaturas}")
    print(f"Média das temperaturas: {media:.2f} °C")
else:
    print("\nNenhuma temperatura foi informada.")
