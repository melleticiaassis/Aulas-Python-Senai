# aprovado e reprovado

def verificar_situacao(media):
    if  media >= 7:
        return"Aprovado"
    else :
        return "reprovado"
    
media = 8
resultado = verificar_situacao(media)
print(resultado)
