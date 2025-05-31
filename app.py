import streamlit as st
import json
from agents.classifier_agent import ClassifierAgent
from memory.redis_memory import SharedMemory

def main():
    st.title("Multi-Agent AI System")
    st.write("Drop your Email text or JSON input, and see what the agents say!")

    memory = SharedMemory()
    classifier = ClassifierAgent(memory)

    input_type = st.radio("Choose input type:", ["Email (text)", "JSON"])

    user_input = None
    if input_type == "Email (text)":
        user_input = st.text_area("Paste your email content here:")
    else:
        user_input_str = st.text_area("Paste your JSON here:")
        if user_input_str:
            try:
                user_input = json.loads(user_input_str)
            except json.JSONDecodeError:
                st.error("Invalid JSON! Please check your input.")

    if st.button("Process Input"):
        if user_input:
            result = classifier.process(user_input, source_id="user-input")
            if result:
                st.success("Processing done!")
                st.json(result)
            else:
                st.warning("No agent available for this input format.")
        else:
            st.error("Please provide input to process.")

if __name__ == "__main__":
    main()
