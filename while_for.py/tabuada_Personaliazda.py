valor_tabuada = int(input("Digite o número da tabuada que deseja calcular: "))
inicio = int(input("Digite um número onde a tabuada deve começar: "))
final = int(input("Digite um número onde a tabuada deve terminar: "))

while inicio <= final :
    print(f" {valor_tabuada*inicio}")
    inicio +=1
