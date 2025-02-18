function envoyerQuestion() {
    let userInput = document.getElementById("user-input").value;
    let chatBox = document.getElementById("chat-box");

    if (userInput.trim() === "") return; // Ne rien envoyer si le champ est vide

    // Affiche la question de l'utilisateur
    let userMessage = document.createElement("div");
    userMessage.innerHTML = `<strong>Vous:</strong> ${userInput}`;
    chatBox.appendChild(userMessage);

    // Envoie la requête au serveur Flask
    fetch("/chatbot", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Affiche la réponse du bot
        let botMessage = document.createElement("div");
        botMessage.innerHTML = `<strong>🤖 Chatbot:</strong> ${data.réponse}`;
        chatBox.appendChild(botMessage);

        // Efface le champ texte
        document.getElementById("user-input").value = "";
        
        // Scroll en bas de la chatbox
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error("Erreur:", error));
}
