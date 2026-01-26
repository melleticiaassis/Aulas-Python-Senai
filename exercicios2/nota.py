

nota = float(input("Digite uma nota entre 0 a 10: "))

while nota < 0 or nota > 10:
    print(f"A nota {nota} é inválida.")
    nota = float(input("Digite novamente uma nota entre 0 a 10: "))
        

    