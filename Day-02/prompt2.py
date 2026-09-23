import ollama
response = ollama.chat(
    model"llama3.2:3b",
    messages=[ 
        {
            "role":"user",
            "content": "Defination of AI .Give three types of AI with examples in six lines?"
        }
    ]
)
print(response["message"]["content"])