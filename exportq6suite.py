import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("question6.csv")

# Supprimer les colonnes "neutral" et "city"
df = df.drop(columns=['neutral', 'city'])

# Filtrer le DataFrame pour inclure uniquement les lignes où les colonnes "home_team" et "country" sont identiques
df = df[df['home_team'] == df['country']]

# Écrire le résultat dans un nouveau fichier CSV
df.to_csv("question6filtre.csv", index=False)
