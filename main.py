"""
This script is used to test the OllamaLLM model.
"""
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from tools import insert_data, read_data, update_data, fetch_schema, create_table

llm = ChatOllama(
    model="llama3:8b",
    temperature=0,
    base_url="http://127.0.0.1:11434",
)

memory = ConversationBufferMemory(memory_key="chat_history")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}"),
])

agent = initialize_agent(
    tools=[insert_data, read_data, update_data, fetch_schema, create_table],
    llm=llm,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True,
)


if __name__ == "__main__":
    while True:
        input_text = input("Enter your message (q to quit): ")
        if input_text == "q":
            break
        response = agent.invoke({"input": input_text})
        print(response.content)
