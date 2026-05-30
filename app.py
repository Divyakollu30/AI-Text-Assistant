import streamlit as st
from google import genai

# 1. Setup the Web Page Title
st.title("🤖 AI Text Assistant")
st.write("Paste your text below and let AI summarize it or answer questions!")

# 2. Ask the user for their free Gemini API Key
# (You get this from Google AI Studio completely free)
api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    # Initialize the Google GenAI client
    client = genai.Client(api_key=api_key)
    
    # 3. Input Box for the large text
    user_text = st.text_area("Paste your long text/article here:", height=200)
    
    # 4. Create two simple buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✨ Summarize Text"):
            if user_text:
                # Ask Gemini to summarize
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"Summarize the following text in 3 bullet points:\n\n{user_text}"
                )
                st.subheader("Summary:")
                st.write(response.text)
            else:
                st.warning("Please paste some text first!")
                
    with col2:
        # Input for a specific question about the text
        question = st.text_input("Ask a question about this text:")
        if st.button("🔍 Answer Question"):
            if user_text and question:
                # Ask Gemini to answer based on the text
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"Based on this text:\n{user_text}\n\nAnswer this question: {question}"
                )
                st.subheader("AI Answer:")
                st.write(response.text)
            else:
                st.warning("Please provide both the text and a question!")
else:
    st.info("Please enter your Gemini API Key to activate the assistant.")