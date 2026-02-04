import streamlit as st

st.title("Calculadora de tabuada")

numero_tabuada = st.number_input("Digite o valor da tabuada: ")
inicio_tabuada = st.number_input("Digite o inicio da tabuada: ")
final_tabuada = st.number_input("Digite o final da tabuada: ")

if st.button("Mostra a tabuada"):
    for multiplicador in range(inicio_tabuada, final_tabuada ):
        st.markdown(f"**{numero_tabuada} X {multiplicador} = {final_tabuada * multiplicador}**")