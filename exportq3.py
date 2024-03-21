import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("results.csv")

# Supprimer les lignes contenant "Friendly" dans la colonne "tournament"
df = df[df['tournament'] != 'Friendly']

# Supprimer les colonnes spécifiées
df = df.drop(columns=["date", "city", "country", "neutral"])

# Créer un nouveau DataFrame pour les équipes à domicile
home_teams = df.groupby(['home_team', 'tournament']).agg({'home_score': 'sum'}).reset_index()
home_teams.columns = ['country', 'tournament', 'goals']

# Créer un nouveau DataFrame pour les équipes à l'extérieur
away_teams = df.groupby(['away_team', 'tournament']).agg({'away_score': 'sum'}).reset_index()
away_teams.columns = ['country', 'tournament', 'goals']

# Fusionner les DataFrames home_teams et away_teams
all_teams = pd.concat([home_teams, away_teams], ignore_index=True)

# Regrouper les données par équipe et par compétition, puis calculer le nombre total de buts
total_goals_per_country_tournament = all_teams.groupby(['country', 'tournament'])['goals'].sum().reset_index()

# Nom du fichier CSV exporté
export_file = "question3.csv"

# Écrire les données dans un nouveau fichier CSV en renommant la colonne
total_goals_per_country_tournament.to_csv(export_file, index=False)

# Afficher le nom du fichier CSV exporté
print("Fichier CSV exporté:", export_file)
