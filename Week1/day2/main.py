import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key khaa hai  bhai")
client = Groq(api_key = my_api_key)
model  = "llama-3.3-70b-versatile"
role_system = "system"
role = "user"
prompt_system = input("TYPE THE MESSAGE, YOU WANT TO BE THE SYSTEM AS :")
prompt = input("TYPE YOUR MESSAGE HERE: ")
message_system = {

    "role" : role_system,
    "content" : prompt_system
}
message = {
    "role" : role,
    "content" : prompt
}
messages = [message_system,message]
response = client.chat.completions.create(model=model, messages=messages, temperature = 2)
print(response)

print ("############################################################################################")

answer = response.choices[0].message.content
print(answer)