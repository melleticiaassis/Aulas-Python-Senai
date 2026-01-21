ganha_por_hora = float(input("Digite quanto você ganha por hora: "))
ganha_por_mes = float(input("Digite quanto você ganha por mês: "))
valor_salario = ganha_por_hora*ganha_por_mes
# .3f limita as casas decimais 
print (f"Seu salário por mensal é de {valor_salario: .3f}")