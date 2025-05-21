import streamlit as st

st.title("🎈 hai barudawgh")
st.write(
    "kayek noyek lucu kata aleta."
)
st.header("noycayek")
st.image("IMG_0502.jpeg")
st.write("\n")
st.title("aplikasi sederhana")
st.header("aplikasi mengecek nilai ganjil/genap")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.write(f"{angka} asalah angka ganjil")
    
