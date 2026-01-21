nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeia nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3= float(input("Digite sua treceira nota: "))

media = (nota1*nota2*nota3)/3
print("media", media)

if media >= 7 :
    print("Você passou!")
elif media <= 4:
    print("Você está em recuperação: ")

else:
    print("Você reprovou")