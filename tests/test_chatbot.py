from chatbot import generer_reponse

def test_generer_reponse():
    prompt = "Quels sont les effets secondaires du Paracétamol ?"
    reponse = generer_reponse(prompt)
    assert isinstance(reponse, str)
