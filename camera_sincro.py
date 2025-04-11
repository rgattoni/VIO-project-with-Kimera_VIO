import csv

def genera_csv(numero_partenza, numero_finale, nome_file="output.csv", lunghezza_desiderata=14):
    """
    Genera un file CSV con due colonne, "filename" e "filename.png".

    Args:
        numero_partenza (int): Il numero di partenza per la prima riga.
        numero_finale (int): Il numero finale fino a cui generare le righe.
        nome_file (str, optional): Il nome del file CSV da creare. Default è "output.csv".
    """

    with open(nome_file, mode='w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(["filename", "filename.png"])  # Scrive l'intestazione

        numero_corrente = numero_partenza
        while numero_corrente <= numero_finale:
            numero_stringa = str(numero_corrente).ljust(lunghezza_desiderata, '0')
            writer.writerow([numero_stringa, f"{numero_stringa}.png"])
            numero_corrente +=50 #prima era 50

# Esempio di utilizzo:
numero_partenza = 69161
numero_finale = 76721
genera_csv(numero_partenza, numero_finale, lunghezza_desiderata=14)
