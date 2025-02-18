import sqlite3

def verifier_stock(nom_medicament):
    conn = sqlite3.connect("pharmacie.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT stock, description FROM medicaments WHERE nom LIKE ?", ('%' + nom_medicament + '%',))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        stock, description = result
        return {"médicament": nom_medicament, "description": description, "stock_disponible": stock}
    else:
        return {"message": f"Le médicament '{nom_medicament}' n'est pas disponible."}
