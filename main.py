"""
This script is used to test the OllamaLLM model.
"""
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model="llama3:8b",
    temperature=0,
    base_url="http://127.0.0.1:11434",
)

messages = [("system", "You are a helpful assistant.")]

while True:
    user_input = input("Enter your message (q to quit): ")
    if user_input == "q":
        break

    messages.append(("user", user_input))

    prompt = ChatPromptTemplate.from_messages(messages)
    chain = prompt | llm

    response = chain.invoke({"input": user_input})
    print(response.content)

    messages.append(("assistant", response.content))
