# app.py
import streamlit as st
from agent import BedrockAgent
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    st.set_page_config(page_title="Bank Sales Assistant", layout="wide")
    st.title("🏦 Bank Sales Assistant")

    # Initialize the agent
    try:
        agent = BedrockAgent(
            name='SalesAssistantAgent',
            model_id='anthropic.claude-v3.sonnet',
            region_name='us-east-1'
        )
    except Exception as e:
        st.error("Failed to initialize the Bedrock agent. Please check your AWS configuration.")
        logging.error(f"Agent initialization error: {e}")
        return

    # Initialize session state
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    # Sidebar for user input
    with st.sidebar:
        st.header("Chat with the Assistant")
        user_input = st.text_input("You:", key='user_input')
        send_button = st.button("Send")

    # Main conversation display
    st.subheader("Conversation")
    conversation_placeholder = st.empty()

    if send_button and user_input.strip():
        # Append user input to conversation
        st.session_state.conversation.append(("You", user_input))

        # Generate agent response
        with st.spinner('Assistant is typing...'):
            response = agent.generate_response(user_input)
        st.session_state.conversation.append(("Assistant", response))

        # Clear input field
        st.session_state.user_input = ''

    # Display conversation
    with conversation_placeholder.container():
        for speaker, message in st.session_state.conversation:
            if speaker == "You":
                st.markdown(f"**{speaker}:** {message}")
            else:
                st.markdown(
                    f"<div style='background-color:#f0f2f6; padding:10px; border-radius:5px;'>"
                    f"<strong>{speaker}:</strong> {message}</div>",
                    unsafe_allow_html=True
                )

if __name__ == "__main__":
    main()
