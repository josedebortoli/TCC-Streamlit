import streamlit as st

st.tile("Hello, Streamlit!")
st.header("Welcome to Streamlit")
st.subheader("This is a simple Streamlit app.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")

number = st.number_input("Enter a number:", min_value=0, max_value=100)
st .write(f"You entered the number: {number}")