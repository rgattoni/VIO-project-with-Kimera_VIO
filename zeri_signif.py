import pandas as pd

def aggiungi_zeri_colonna_csv(nome_file, lunghezza_desiderata):
    """
    Aggiunge un certo numero di zeri all'inizio dei valori nella prima colonna
    di un file CSV.

    Args:
        nome_file (str): Il percorso del file CSV da modificare.
        numero_zeri (int): Il numero di zeri da aggiungere.
    """
    try:
        # Leggi il file CSV
        df = pd.read_csv(nome_file)

        # Verifica che il DataFrame non sia vuoto e abbia almeno una colonna
        if df.empty or df.shape[1] < 1:
            print(f"Errore: Il file CSV '{nome_file}' è vuoto o non ha colonne.")
            return

        # Seleziona la prima colonna
        prima_colonna = df.iloc[:, 0]

        # Converti i valori della prima colonna in stringhe e aggiungi gli zeri
        df.iloc[:, 0] = prima_colonna.astype(str).apply(lambda x: x.ljust(lunghezza_desiderata, '0'))

        # Salva il DataFrame modificato nello stesso file CSV (sovrascrivendo)
        df.to_csv(nome_file, index=False)

        print(f"Operazione completata con successo. Aggiunti zeri meno significativi alla prima colonna del file '{nome_file}'.")

    except FileNotFoundError:
        print(f"Errore: Il file '{nome_file}' non è stato trovato.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

# Esempio di utilizzo:
nome_del_file_csv = "data_aggiungi_zeri.csv"  # Sostituisci con il nome del tuo file CSV
lunghezza_finale_desiderata = 14
aggiungi_zeri_colonna_csv(nome_del_file_csv, lunghezza_finale_desiderata)
