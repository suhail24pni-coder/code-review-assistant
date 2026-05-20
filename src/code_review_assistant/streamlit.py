import streamlit as st
from code_review_assistant.crew import CodeReviewAssistantCrew

# 1. Page Configuration
st.set_page_config(page_title="AI Code Review Assistant", page_icon="💻", layout="wide")

st.title("💻 AI Code Review Assistant")
st.markdown("Paste your Python function or module below to receive a deep-dive review from a team of virtual Senior Engineers.")

# 2. Sidebar configuration for credentials/settings if needed
st.sidebar.header("Settings")
st.sidebar.markdown("This assistant uses your configured environment LLM to review code.")

# 3. User Input
code_input = st.text_area(
    "Enter your Python code here:", 
    height=250, 
    placeholder="def my_function():\n    labels = []\n    ...\n    return labels"
)

# 4. Trigger the Crew Execution
if st.button("🚀 Analyze Code", type="primary"):
    if not code_input.strip():
        st.warning("Please paste some code first!")
    else:
        with st.spinner("🕵️ The crew is analyzing your code (Hunting bugs, checking style, and refactoring)..."):
            try:
                # Format inputs for the crew
                inputs = {
                    'code_input': code_input
                }
                
                # Run the CrewAI kickoff
                crew_output = CodeReviewAssistantCrew().crew().kickoff(inputs=inputs)
                
                st.success("✅ Analysis Complete!")
                
                # 5. Display Resulting Markdown Output
                st.markdown("## 📄 Code Review Report")
                # Using standard string conversion from CrewOutput
                st.markdown(str(crew_output))
                
            except Exception as e:
                st.error(f"An error occurred during execution: {e}")