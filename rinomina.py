import os
import csv

# Specifica il percorso del file CSV e della cartella contenente i file .png
csv_file = 'data.csv'
data_folder = 'data'

# Legge le stringhe dal file CSV.
# Assumiamo che ogni riga del CSV sia nel formato:
#   nomefile.png,numero
rename_values = []
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i,row in enumerate(reader):
        # salta la prima riga
        if i == 0:
            continue
        if len(row) < 2:
            continue  # salta eventuali righe non conformi
        # Prende la stringa della seconda colonna, rimuovendo eventuali spazi
        new_name = row[1].strip()
        rename_values.append(new_name)

# Recupera e ordina la lista dei file .png dalla cartella 'data'
png_files = [file for file in os.listdir(data_folder) if file.lower().endswith('.png')]
png_files.sort()  # Assicurati di avere un ordinamento consistente

# Verifica che il numero di file corrisponda al numero di nomi nel CSV
if len(rename_values) != len(png_files):
    print("Attenzione: il numero delle righe nel CSV ({}) non corrisponde al numero dei file .png ({})".format(len(rename_values), len(png_files)))

# Rinomina i file uno per uno
for i, file in enumerate(png_files):
    if i >= len(rename_values):
        break  # se per qualche motivo ci fossero più file che record, interrompe
    old_path = os.path.join(data_folder, file)
    # Costruisce il nuovo nome aggiungendo l'estensione .png
    new_filename = rename_values[i]
    new_path = os.path.join(data_folder, new_filename)
    os.rename(old_path, new_path)
