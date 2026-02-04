import streamlit as st

st.title("Cadrasto 💕")

nome_usuario = st.text_input("Digite o seu nome de usuario")
email = st.text_input("Digite o seu email: ")
senha = st.text_input("Digite sua senha: ")
senha_confirma = st.text_input("Comfirme seua senha: ")

if st.button("Cadratar"):
    #validação da senha
    if senha == senha_confirma:
        with open("./pessoa.txt", "a") as arquivo:
            arquivo.write(f"Nome: {nome_usuario:>20} | E-mail: {email:>20} Senha: {senha:>20}  \n")
        st.success("Cadrasto Comfirmado!")






# if st.text("E-mail"):
#     st.success("")