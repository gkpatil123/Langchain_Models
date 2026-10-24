from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model='gpt-4', temperature=0.7, max_tokens=1000)

result = chat.invoke("what is the capital of india?")

print(result.content)
