import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

model = ChatGroq(model="llama-3.3-70b-versatile")

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a professional email writer. 
Write a complete professional email with:
- Subject line
- Greeting
- Body
- Closing & Signature

Keep the tone appropriate for the recipient type.
Be concise, clear and professional."""),
    
    ("human", "Write a professional email on subject: {subject}, addressed to: {to_whom}")
])

st.title("Smart Professional Email Generator")

subject = st.text_input("Enter the subject of your mail:")
to_whom = st.text_input("To whom are you sending? (HR, colleague, Junior, etc):")

if st.button("Generate Email"):
    if not subject or not to_whom:
        st.error("Subject and recipient cannot be empty!")
    else:
        final_prompt = prompt.invoke({
            "subject": subject,
            "to_whom": to_whom
        })

        response = model.invoke(final_prompt)

        st.subheader("Generated Email:")
        st.text(response.content)
        st.code(response.content, language="text")