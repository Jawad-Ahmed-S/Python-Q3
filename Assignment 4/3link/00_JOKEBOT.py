import streamlit as st;
JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = 'Sorry I only tell jokes'

st.title("Joke Bot")
user_Input= st.text_input("Enter your Command");


if user_Input.lower().strip() == 'joke':
    st.write(JOKE)
elif user_Input:
    st.write(SORRY)
