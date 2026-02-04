import streamlit as st

st.title("Calculadora Simples ❤️")
st.subheader("Feito com streamlit 💕")

valor1 = st.number_input("Digite o primeiro valor: ", value=0)
valor2 = st.number_input("Digite o valor a ser somado: ",value=0 )

opcao = st.selectbox(
    "Qual opção deseja realizar? ",
    ( "Soma", "Subtração", "Multiplição","Divisão" ))
try: 
    if opcao == "Soma":
        if st.button("Calcular"):
            st.success(f"{valor1 + valor2}")

    elif opcao == "Subtração":
        if st.button("Calcular"):
            st.success(f"{valor1 - valor2}")


    elif opcao == "Multiplição":
        if st.button("Calcular"):
            st.success(f"{valor1 * valor2}")

    elif opcao == "Divisão":
        if st.button("Calcular"):
         st.success(f"{valor1 / valor2}")

except: 
    st.text("Opção inválida ")