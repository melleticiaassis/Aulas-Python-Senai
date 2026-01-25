valor = int(input("Digite a nota que deseja calcular: "))

print("Notas de 100:", valor // 100)
valor = valor % 100

print("Notas de 50:", valor // 50)
valor = valor % 50

print("Notas de 20:", valor // 20)
valor = valor % 20

print("Notas de 10:", valor // 10)
valor = valor % 10

print("Notas de 5:", valor // 5)
valor = valor % 5

print("Notas de 2:", valor // 2)
valor = valor % 2

print("Notas de 1:", valor // 1)
