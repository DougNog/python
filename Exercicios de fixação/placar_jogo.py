time1 = int(input("Digite o número de gols do time 1: "))
time2 = int(input("Digite o número de gols do time 2: "))

if time1 > time2:
    print("O time 1 venceu!")
elif time2 > time1:
    print("O time 2 venceu!")
else: 
    print("Empate!")
    
print("Placar final: {} x {}".format(time1, time2))