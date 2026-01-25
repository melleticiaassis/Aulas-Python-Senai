#Média com condição de parada

soma = 0
quantidade = 0

while True:
    valor = int(input("Digite um número (-1 para parar): "))
    
    if valor == -1:
         break  # é usado pra quebrar e sair do loop se o usuário digitar -1, e aplica pro for 
    soma += valor        # soma = soma + valor
    quantidade += 1      # somar 1 á quantidade 
    
    if quantidade > 0 :
        media = soma / quantidade
        print("A soma dos números são: ", media)
    else:
        print("Valor não encontrado")
    
