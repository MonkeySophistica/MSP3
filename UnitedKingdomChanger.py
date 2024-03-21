import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("question3.csv")

# Remplacer les valeurs "England" par "United Kingdom" dans la colonne "country"
df['country'] = df['country'].replace('England', 'United Kingdom')

# Écrire les données dans un nouveau fichier CSV
df.to_csv("question3clean.csv", index=False)
