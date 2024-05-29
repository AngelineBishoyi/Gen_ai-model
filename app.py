
#import mysql.connector
#conn = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #password="root",
    #database="name"
#)
#cursor = conn.cursor()

# Insert sample data
#data = [
    #('Noa', 'Hernandez', '24 Maple Street', 'Detroit', 'MI', 48226),
    #('Noah', 'Hernande', '24 Maple Street', 'Detroit', 'MI', 48226),
     #('Noahh', 'Hernandez', '24 Maple Street', 'Detroit', 'MI', 48226),
    #('N.', 'Hernandez', '24 Maple Street', 'Detroit', 'MI', 48226),
    #('Noah', 'Hern', '24 Maple Street', 'Detroit', 'MI', 48226),
    #('Noah Hernandez', '', '24 Maple Street', 'Detroit', 'MI', 48226),
    #('Liam', 'Johnson', '10 Elm Street', 'Chicago', 'IL', 60610),
    #('Noah Alex', 'Hernandez', '24 Maple Street', 'Detroit', 'MI', 48226),
    #('Noeh', 'Hernandez', '24 Maple Street', 'Detroit', 'MI', 48226),
    #('Noah', 'Mr. Hernandez', '24 Maple Street', 'Detroit', 'MI', 48226),
    #('Ethan', 'Miller', '5 Oak Lane', 'Austin', 'TX', 78704),
    #('Noah', 'Hernande', '24 Maple Street', 'Detroit', 'MI', 48226),
    #('David', 'Williams', '12 Main Street', 'Seattle', 'WA', 98104),
    #('Noahh', 'Hernandez', '24 Maple Street', 'Detroit', 'MI', 48226)
#]
#insert_query = "INSERT INTO test (first_name, last_name, address, city, state, zip_code) VALUES (%s, %s, %s, %s, %s, %s)"
#cursor.executemany(insert_query, data)

# Commit changes
#conn.commit()
#print("Inserted")


import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import os

load_dotenv()

st.set_page_config(
    page_title="Chat with Gemini Pro",
    page_icon=":brain:",
    layout="centered"
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel("gemini-pro")

def translate_Streamlit(user_role):
    if user_role == "model":
        return "assistance"
    else:
        return user_role

# Session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Title
st.title("Gemini Pro chatbot")

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_Streamlit(message.role)):
        st.markdown(message.parts[0].text)

# User input
user_prompt = st.chat_input("Ask me anything")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini's response
    with st.chat_message("assistance"):
        st.markdown(gemini_response.text)
