from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='qwen3:0.6b', messages=[
  {
    'role': 'system',
    'content': """You are a coder""",
  },
  {
    'role': 'user',
    'content': 'write a hello daddy with python?',
  },
])
# or access fields directly from the response object
print(response.message.content)