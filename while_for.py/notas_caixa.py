# Simulador de Caixa Eletrônico
# Calcula o menor número de notas para um valor informado

valor = int(input("Digite o valor do saque: "))

# Cálculo das notas de 100
print("Notas de 100:", valor // 100)
valor %= 100

# Cálculo das notas de 50
print("Notas de 50:", valor // 50)
valor %= 50

# Cálculo das notas de 20
print("Notas de 20:", valor // 20)
valor %= 20

# Cálculo das notas de 10
print("Notas de 10:", valor // 10)
valor %= 10

# Cálculo das notas de 5
print("Notas de 5:", valor // 5)
valor %= 5

# Cálculo das notas de 2
print("Notas de 2:", valor // 2)
valor %= 2

# O valor restante corresponde às notas de 1
print("Notas de 1:", valor)
