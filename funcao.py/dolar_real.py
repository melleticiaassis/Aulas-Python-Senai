
# conversão de dólar para real
cotacao_dolar = 5

def dolar_real(qtd_dolar):
    return qtd_dolar * cotacao_dolar

# conversão de real para dólar
def real_dolar(qtd_real):
    return qtd_real / cotacao_dolar

# opção menu
# ler a escolha do usuario 
# decidir oque fazer com base na escolha
opcao = int(input("[1] - Converter Dólar para Real\n [2] - Converter Real para Dólar\n [3] - Sair\n"))


# realizar a conversão
if opcao == 1:
    dolar = float(input("Digite a quantidade em Dólar: "))
    resultado = dolar_real(dolar)
    #.2f serve pra dininuir os números na resposta
    print(f"Valor em Reais: R$ {resultado:.2f}")

elif opcao == 2:
    real = float(input("Digite a quantidade em Reais: "))
    resultado = real_dolar(real)
    #.2f serve pra dininuir os números na resposta
    print(f"Valor em Dólar: US$ {resultado:.2f}")

elif opcao == 3:
    print("Saindo do programa...")

else:
    print("Opção inválida!")

