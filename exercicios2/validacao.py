#Nome: maior que 3 caracteres
#Idade: entre 0 e 150; 
#SC: maior que zero; 
#Sexo: 'f' ou 'm'; 
#Estado Civil: 's', 'c', 'v', 'd';
print("Olá!")
nome = input("Digite seu nome: ")
while len(nome) <3:
    print("Não é permitido nomes com menos de 3 caracteres.")
    nome = input("Digite um nome com mais de 3 letras: ")

idade = float(input("Digite seu idade: "))
while idade < 0 or idade > 150:
    print("Idade maior que 150 inválido.")
    idade = float(input("Digite sua idade até 150: "))

salario = float(input("Digite seu salário: "))
while salario >= 0 :
    print("Não é permitido salário igual ou menor a 0.")
    salario = float(input("Digite um salário sendo maior que 0: "))

sexo = input("Digite seu sexo F pra femenino e M pra masculino: ").upper
while sexo == "F" or sexo == "M":
    print("Sexo inválido.")
    sexo = input("Por favor digite novamente seu sexo, F pra femenino e M pra masculino: ").upper

estado_civil = input("Digite seu Estado Civil, S prra solteiro(a), C para casado(a), V para viuvo(a), D para divorciado(a)").upper
while estado_civil == "S" or estado_civil == "C" or estado_civil == "V" or estado_civil == "D":
    print("Estado Civil inválido, digite novamente")
    estado_civil =  input("Digite novamente ")