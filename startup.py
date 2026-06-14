import ollama
import streamlit as st

st.set_page_config(page_title="Startup Idea Validator", page_icon="🚀")

st.title("🚀 AI Startup Idea Validator")
st.write("Enter your startup idea and get a detailed analysis.")

idea = st.text_area(
    "Describe your startup idea",
    placeholder="Example: AI-powered attendance system for colleges"
)

def startup_validator(idea):
    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'system',
                'content': """
You are an expert startup advisor, entrepreneur, and investor.

Analyze startup ideas using the following format:

🚀 Idea Score (0-100)

🎯 Problem Being Solved

👥 Target Audience

📈 Market Potential
(Low / Medium / High)

⚔ Competition Level
(Low / Medium / High)

💰 Revenue Models
(List at least 3)

⭐ Unique Selling Points (USP)

⚠ Risks and Challenges

🔧 Suggestions for Improvement

💵 Investor Decision
Would you invest? (YES/NO)

📝 Final Verdict

Be realistic and critical.
Do not blindly praise ideas.
Provide actionable suggestions.
"""
            },
            {
                'role': 'user',
                'content': idea
            }
        ]
    )

    return response['message']['content']

if st.button("Analyze Startup Idea"):
    if idea.strip():
        with st.spinner("Analyzing your startup idea..."):
            result = startup_validator(idea)

        st.subheader("📊 Analysis Report")
        st.write(result)
    else:
        st.warning("Please enter a startup idea first.")