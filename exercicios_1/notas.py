nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeia nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1*nota2)/3
print("media", media)

if media >= 7 :
    print("Você passou!")
elif media <= 7:
    print("Você está em recuperação: ")
elif media == 10 :
    print("Aprovação com distinção")
