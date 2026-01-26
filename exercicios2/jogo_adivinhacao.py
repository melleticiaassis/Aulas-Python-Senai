
import random

numero_magico= random.randint(0,50)

numero_usuario = int(input("Descubra oo número sorteado (0 - 50): "))
while numero_usuario!=numero_magico:
    if numero_magico > numero_usuario:
        print("O número sorteado é maior.")
    elif numero_magico > numero_usuario:
        print("O número sorteado é menor.")

    numero_usuario = int(input("Digite novamente: "))
print("Você acertou!")
