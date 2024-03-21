import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("results.csv")

# Liste des tournois à inclure
tournois_inclus = ["Copa América", "AFC Asian Cup", "African Cup of Nations", "FIFA World Cup", "UEFA Euro"]

# Filtrer le DataFrame pour inclure uniquement les tournois de la liste
df = df[df['tournament'].isin(tournois_inclus)]

# Fonction pour déterminer la victoire à domicile
def determine_victoire(home_score, away_score):
    return home_score > away_score

# Appliquer la fonction pour chaque ligne
df['victoire'] = df.apply(lambda row: determine_victoire(row['home_score'], row['away_score']), axis=1)

# Écrire le résultat dans un nouveau fichier CSV
df.to_csv("question6.csv", index=False)
