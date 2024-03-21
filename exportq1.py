import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("results.csv")

# Convertir la colonne 'date' en format datetime
df['date'] = pd.to_datetime(df['date'])

# Filtrer les lignes pour ne garder que celles entre 2000 et 2010
df = df[(df['date'].dt.year >= 2000) & (df['date'].dt.year <= 2010)]

# Supprimer les colonnes spécifiées
df = df.drop(columns=["tournament", "city", "country"])

# Filtrer les lignes pour ne garder que celles où 'neutral' est TRUE
df = df[df['neutral'] == False]

# Écrire les données dans un nouveau fichier CSV
df.to_csv("question1.csv", index=False)
