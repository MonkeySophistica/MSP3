import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("results.csv")

# Fonction pour déterminer le pays gagnant ou un match nul
def determine_gagnant(home_team, away_team, home_score, away_score):
    if home_score > away_score:
        return home_team
    elif away_score > home_score:
        return away_team
    else:
        return 'Match nul'

# Appliquer la fonction pour chaque ligne et ajouter la colonne "gagnant"
df['gagnant'] = df.apply(lambda row: determine_gagnant(row['home_team'], row['away_team'], row['home_score'], row['away_score']), axis=1)

# Supprimer les lignes où la colonne "gagnant" est "Match nul"
df = df[df['gagnant'] != 'Match nul']

# Réinitialiser les indices après la suppression des lignes
df = df.reset_index(drop=True)

# Convertir la colonne "date" en datetime
df['date'] = pd.to_datetime(df['date'])

# Créer une fonction pour déterminer l'époque en fonction de l'année
def determine_epoque(year):
    start_year = 1873
    epoque_duration = 20
    num_epochs = (year - start_year) // epoque_duration
    epoch_start = start_year + num_epochs * epoque_duration
    if epoch_start + epoque_duration - 1 > 2023:  # Vérifier si l'époque dépasse 2023
        epoch_end = 2023  # Utiliser 2023 comme année de fin
    else:
        epoch_end = epoch_start + epoque_duration - 1  # Utiliser la formule normale
    return f"{epoch_start} à {epoch_end}"

# Appliquer la fonction pour chaque ligne et ajouter la colonne "epoque"
df['epoque'] = df['date'].dt.year.apply(determine_epoque)

# Regrouper par équipe et par époque, puis compter les victoires par équipe par époque
victoires_par_epoque = df.groupby(['epoque', 'gagnant']).size().reset_index(name='nombre_de_victoires')

# Écrire le résultat dans un nouveau fichier CSV
victoires_par_epoque.to_csv("question4.csv", index=False)
