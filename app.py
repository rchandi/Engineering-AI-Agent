import streamlit as st

st.title("Engineering AI Copilot")

st.write("Welcome to your engineering assistant.")

user_input = st.text_area("Enter your engineering question")

if st.button("Submit"):

    st.write("You asked:")
    st.write(user_input)

    st.write("Response:")
    st.write("AI analysis will appear here.")
