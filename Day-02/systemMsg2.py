import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[ 
        {
            "role":"system",
            "content":"Give answer in two lines only for five year old"
        },
        {
            "role":"user",
            "content": "what is AI"
        }
    ]
)
print(response["message"]["content"])