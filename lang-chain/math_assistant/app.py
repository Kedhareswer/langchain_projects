# app.py
import os
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
from sympy_tools import sympy_derivative_tool, sympy_integral_tool

# Load .env variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Init LLM
llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")

# Agent
tools = [sympy_derivative_tool, sympy_integral_tool]
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# --- UI ---
st.title("🧠 Math Assistant with LangChain + Groq")
query = st.text_input("🔢 Ask a math question (e.g., 'differentiate sin(x)*x**2')")

if query:
    with st.spinner("🤖 Computing..."):
        try:
            answer = agent.run(query)
            st.success("✅ Done")
            st.markdown(f"**Answer:** {answer}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
