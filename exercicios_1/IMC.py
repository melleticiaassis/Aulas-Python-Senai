altura = float(input("Digite a sua altura: "))
peso = float(input("Digite a sua peso: "))

imc = peso/(altura*altura)
print(f"Seu peso é {imc:.2f}:")

if imc >= 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print ("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade Grau 1")
elif imc <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")