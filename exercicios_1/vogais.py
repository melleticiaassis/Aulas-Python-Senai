# . upper() pra deixar as letras maiusculas 
# \ pra eviatr quebra de linha.

letra = input("Digite a letra que deseja: ").upper()

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("Vogal!")
else:
    print("Consoante")