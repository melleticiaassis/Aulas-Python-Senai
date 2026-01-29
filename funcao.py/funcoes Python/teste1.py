# Parâmetros - variáveis do programa principal
def calcular_media(n1, n2, n3):
    # media criada dentro da função não existe fora
    media = (n1 + n2 + n3) / 3
    # return ->  devolve valor
    return media

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))

# sempre guardar o retorno numa variável
resultado = calcular_media(nota1, nota2, nota3)

print(f"Sua média é {resultado}")

# o return volta e cai dentro de resultado
