nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
possui_carteira = int(input("Possui carteira de motorista?\n(1-SIM / 2-NÃO)"))

if idade >= 18:

    if possui_carteira == "1":
        print("Pode dirigir.")
    else:
        print() 


else:
   print("menor de 18 anos")