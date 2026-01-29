# Calcula maior e menor valor de um número.

def maior_numero (n1 , n2):
    if n1 > n2 :
        return n1
    else:
        return n2
    
numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite um valor: "))
resultado = maior_numero(numero1,numero2)

print(F"O valor é maior valor é o {resultado}")

