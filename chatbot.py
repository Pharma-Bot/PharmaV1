from transformers import pipeline

# Chargement du modèle de question-réponse médical
modele_qa = pipeline("question-answering", model="dmis-lab/biobert-base-cased-v1.1")

def generer_reponse(question):
    """Génère une réponse fiable à partir d'une base de connaissances médicale."""
    
    contexte = """
    Le paracétamol est un analgésique utilisé pour traiter la douleur et la fièvre.
    L'ibuprofène est un anti-inflammatoire utilisé pour soulager les douleurs légères à modérées.
    En cas de maux de tête fréquents, il est conseillé de boire de l'eau, se reposer et éviter le stress.
    Consultez un médecin si les symptômes persistent.
    """
    
    resultat = modele_qa({"question": question, "context": contexte})
    
    if "answer" in resultat:
        return resultat["answer"]
    else:
        return "Je ne suis pas sûr, veuillez consulter un professionnel de santé."

# Test rapide
if __name__ == "__main__":
    while True:
        question = input("Posez votre question : ")
        if question.lower() in ["exit", "quit", "stop"]:
            break
        print("🤖", generer_reponse(question))
