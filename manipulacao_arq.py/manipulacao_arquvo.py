# nome = input("Digite o nome: ")
# email = input("Digite o e-mail: ")

# with open("./pessoa.txt", "a") as arquivo:
#     arquivo.write(f"NOme: {nome} | E-mail: {email}\n")


nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")
cidade = input("Digite a cidade onde reside ")

with open("./pessoa.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome: > 20} | E-mail: {email: > 20} Codade: {cidade}\n")