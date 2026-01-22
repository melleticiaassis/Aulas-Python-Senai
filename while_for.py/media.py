soma = 0
contador = 0

numero = int(input("Digite um número (-1 para parar): "))

while numero != -1:
    soma = soma + numero
    contador = contador + 1
    numero = int(input("Digite um número (-1 para parar): "))

if contador > 0:
    media = soma / contador
    print("Média:", media)
else:
    print("Nenhum número válido foi digitado")
