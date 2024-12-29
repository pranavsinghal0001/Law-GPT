import streamlit as st
from utils import create_qa_pipeline

def initialize_session_state():
    """Initialize or reset session state variables"""
    if 'chat_log' not in st.session_state:
        st.session_state.chat_log = []
    
    # Initialize QA pipeline only once
    if 'qa_chain' not in st.session_state:
        with st.spinner('Loading AI model... This might take a moment'):
            st.session_state.qa_chain = create_qa_pipeline()

def main():
    # Set page configuration
    st.set_page_config(page_title="Indian Law Q&A Bot", page_icon="⚖")
    
    # Initialize session state
    initialize_session_state()
    
    # Page title and description
    st.title("🏛 Indian Law Q&A Assistant")
    st.write("Ask questions about Indian Law. Our AI will help you find answers from legal documents.")
    
    # Chat input
    user_input = st.chat_input("Ask a question about Indian Law...")
    
    # Process user input
    if user_input:
        try:
            # Use .invoke() instead of direct call
            response = st.session_state.qa_chain.invoke({"query": user_input})
            bot_output = response.get('result', "I couldn't find an answer to your question.")
            
            # If response is empty or unhelpful, display an error message
            if not bot_output or "Cannot confidently answer" in bot_output:
                bot_output = "I'm sorry, I couldn't find enough information to answer your question."
            
            # Add to chat log
            st.session_state.chat_log.append({
                "User": user_input, 
                "Bot": bot_output
            })
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    # Display chat history
    for exchange in st.session_state.chat_log:
        with st.chat_message("user"):
            st.write(exchange["User"])
        with st.chat_message("assistant"):
            st.write(exchange["Bot"])

if __name__ == "__main__":
    main()