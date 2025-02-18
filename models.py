from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

def repondre_chatbot(message):
    prompt = f"Question: {message}\nRéponse:"
    reponse = chatbot(prompt, max_length=100, num_return_sequences=1)
    return reponse[0]["generated_text"]
