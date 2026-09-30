from sentence_transformers import util, SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
Sentences = [
    "I love playing chess",
    "I enjoy playing soccer",
    "I like eating pizza"
]
sentence_embedding = model.encode(Sentences)
similarity1 = util.cos_sim(sentence_embedding[0], sentence_embedding[2])
print(similarity1.item())