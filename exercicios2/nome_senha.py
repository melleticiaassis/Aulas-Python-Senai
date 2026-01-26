nome =  str(input("Digite seue nome: "))
senha = str(input("Digite sua senha: "))

while senha == nome:
    print(f"Senha {senha} inválida")
    print("Digite seue nome: ")