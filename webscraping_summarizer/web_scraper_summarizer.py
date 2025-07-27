import os
from dotenv import load_dotenv
from newspaper import Article
from langchain.chat_models import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

# Load .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Load LLM
llm = ChatGroq(api_key=GROQ_API_KEY, model="mixtral-8x7b-32768")

# Prompt template for summarization
prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following article in 5 bullet points:\n\n{text}\n"
)

chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit UI
st.title("📰 Web Article Summarizer")

url = st.text_input("Enter article URL:")
if st.button("Summarize"):
    if url:
        try:
            # Extract article
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()  # For keywords

            st.subheader(article.title)
            st.write(f"🕒 Reading time: {article.meta_data.get('reading_time', 'Unknown')} mins")

            # Show extracted info
            with st.expander("📄 Full Article Text"):
                st.write(article.text)

            # Summarize
            with st.spinner("Summarizing..."):
                summary = chain.run(text=article.text)
                st.subheader("🔍 Summary:")
                st.markdown(summary)

            # Optional: show keywords
            st.markdown("### 🏷️ Keywords:")
            st.write(", ".join(article.keywords))

        except Exception as e:
            st.error(f"Failed to summarize the article: {str(e)}")
    else:
        st.warning("Please enter a valid URL.") 