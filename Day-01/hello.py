import ollama
response = ollama.chat(
    model"llama3.2:3b",
    messages=[ 
        {
            "role":"user",
            "content": "Explain machine learing in 40 words"
        }
    ]
)
print(response["message"]["content"])
