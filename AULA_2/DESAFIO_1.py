#média aritimetica 
nota1 = float(input('Digite a promeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print('A média é: {:.2f}'.format(media))

#calcular a hipotenusa 

cat1 = float(input('digite o valor do primeiro cateto '))
cat2 = float(input('digite o valor do segundo cateto '))

hipo = (cat1**2) + (cat2**2)
hipo = hipo**(1/2)
print('a hipotenusa é: ', hipo)

#aumento de salario
salario = float(input('Digite o valor do salario: '))
aumento = float(input('Digite o percentual de aumento: '))

novoSalario = salario + (salario * aumento / 100)
print('O novo salario é: {:.2f}'.format(novoSalario))



