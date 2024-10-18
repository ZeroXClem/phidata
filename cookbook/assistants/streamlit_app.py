import streamlit as st
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

st.title("News from France Poem Generator")

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)

user_input = st.text_input("Enter a topic for news from France:")

if st.button("Generate Poem"):
    if user_input:
        with st.spinner("Generating poem..."):
            response = assistant.run(f"Search for news from France about {user_input} and write a short poem about it.")
        st.markdown(response)
    else:
        st.warning("Please enter a topic.")