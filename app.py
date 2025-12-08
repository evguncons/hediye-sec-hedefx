import streamlit as st

st.set_page_config(layout="wide")
st.title("Şube Satış Lider Tablosu")

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# HTML içeriğini iframe olarak gömme
st.components.v1.html(html_content, height=800, scrolling=True)
