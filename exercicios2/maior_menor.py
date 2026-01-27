maior = None  # Inicializa a variável maior como None

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    if maior is None or numero > maior:  # se o valor maior ainda não tem valor ou numero é maior
        maior = numero
print(f"O maior número digitado é {maior}")
