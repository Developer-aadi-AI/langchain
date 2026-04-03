from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

st.header("Research Tool")

user_input = st.text_input("Enter your Prompt : ")  # here a user can give any prompt of any size, i.e, the user has control and free to search anything, this creates a problem if our model is not trained for the user's input then it may hallucinate.

if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result.content)

