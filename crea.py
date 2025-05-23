import os

# Cartella di destinazione (puoi modificarla se vuoi salvare i file altrove)
cartella = "articoli"

# Crea la cartella se non esiste
os.makedirs(cartella, exist_ok=True)

# Crea i file da Articolo 5 a Articolo 64
for i in range(8, 64):
    nome_file = f"Articolo {i}.html"
    percorso_completo = os.path.join(cartella, nome_file)
    
    # Crea un file vuoto
    with open(percorso_completo, 'w') as file:
        pass  # Non scriviamo nulla, vogliamo solo creare il file

print("File creati con successo.")
