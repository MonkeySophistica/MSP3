import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("results.csv")

# Calculer la différence entre les scores à domicile et à l'extérieur
df['difference'] = df['home_score'] - df['away_score']

# Prendre la valeur absolue de chaque différence
df['difference'] = df['difference'].abs()

# Filtrer les lignes pour ne garder que celles avec une différence d'au moins 2
df = df[df['difference'] >= 2]

# Supprimer les colonnes spécifiées
df = df.drop(columns=["date", "city", "country", "neutral"])

# Nom du fichier CSV exporté
export_file = "question2a.csv"

# Écrire les données dans un nouveau fichier CSV
df.to_csv(export_file, index=False)

# Afficher le nom du fichier CSV exporté
print("Fichier CSV exporté:", export_file)

