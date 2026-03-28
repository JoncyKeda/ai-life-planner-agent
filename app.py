"""
AI Life Planner Agent (Complete)
"""

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_plan(goal, timeline):
    """Generate roadmap and plan."""
    prompt = f"""
    You are a life planning expert.

    Goal:
    {goal}

    Timeline:
    {timeline}

    Create:
    1. Step-by-step roadmap
    2. Weekly plan
    3. Daily actionable tasks
    4. Tips for success

    Keep it clear and structured.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content


def main():
    st.set_page_config(page_title="AI Life Planner", layout="wide")

    st.title("🧠 AI Life Planner Agent")
    st.write("Turn your goals into actionable plans with AI.")

    st.divider()

    # Inputs
    goal = st.text_area("🎯 Enter your goal", height=100)
    timeline = st.selectbox(
        "⏳ Select timeline",
        ["1 Month", "3 Months", "6 Months", "1 Year"]
    )

    if st.button("🚀 Generate Plan"):
        if goal.strip() == "":
            st.warning("Please enter a goal.")
        else:
            with st.spinner("Generating your plan..."):
                plan = generate_plan(goal, timeline)

            st.subheader("📋 Your AI-Generated Plan")
            st.write(plan)


if __name__ == "__main__":
    main()