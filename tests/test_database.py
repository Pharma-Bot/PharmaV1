from database import verifier_stock

def test_verifier_stock():
    resultat = verifier_stock("Paracétamol")
    assert "stock_disponible" in resultat
