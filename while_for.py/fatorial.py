print("Olá!")
n = int(input("Digite um número a ser calculado seu fatorial: "))

if n < 0:
    print("Número inválido")
else:
    fatorial = 1
i = 1
while i <= n:
    fatorial = fatorial*i
    i = i +1
    print("Fatorial:", fatorial)
