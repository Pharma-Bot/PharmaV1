from flask import Flask, request, jsonify, render_template
from chatbot import generer_reponse

app = Flask(__name__)

# Route pour afficher la page web (évite l'erreur 404)
@app.route("/")
def home():
    return render_template("index.html")

# Route pour poser des questions au bot
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"message": "Veuillez poser une question."}), 400
    
    reponse = generer_reponse(question)
    return jsonify({"réponse": reponse})

if __name__ == "__main__":
    app.run(debug=True)
