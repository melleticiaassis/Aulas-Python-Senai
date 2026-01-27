# Função para calcular fatorial
def fatorial(n):          # Passo 1: recebe o número n
    resultado = 1         # Passo 2: começa com 1
    for i in range(1, n+1):  # Passo 3: vai multiplicando do 1 até n
        resultado = resultado * i
    return resultado      # Passo 4: retorna o resultado final
