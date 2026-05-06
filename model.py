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

print("-"*10, "Welcome to Smart Professional Email Generator", "-"*10)

subject = input("Enter the subject of your mail:\n\n").strip()
to_whom = input("To whom are you sending? (HR, colleague, Junior, etc): ").strip()

if not subject or not to_whom:
    print("Subject and recipient cannot be empty!")
else:
    final_prompt = prompt.invoke({
        "subject": subject,
        "to_whom": to_whom
    })

    response = model.invoke(final_prompt)
    print("\n\n",response.content)