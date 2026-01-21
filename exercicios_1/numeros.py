n1 = float(input("Digite o primeiro número "))
n2 = float(input("Digite o segundo número "))
n3 = float(input("Digite o terceiro número "))

if n1 >= n2:
    maior = n1
else:
    maior = n2 

if n3 > maior:
    maior = n3
    print("O maior número é: ", maior)