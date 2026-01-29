# 1 - O que a função recebe → parâmetros
# 2 - ela faz o calculo/decisão
# 3 - ela devolveo return
# 4 - e o input e print fica fora da função
# 5 - mostre o resultado


def soma (a,b):
    soma = a + b
    return soma

valor1 = int(input("Digite um valor "))
valor2 = int(input("Digite um valor "))

resultado = soma (valor1, valor2)
print (resultado)

