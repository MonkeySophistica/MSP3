import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("results.csv")

# Créer une liste de tous les pays uniques dans les colonnes home_team et away_team
all_teams = set(df['home_team'].unique()).union(set(df['away_team'].unique()))

# Filtrer les lignes où le pays dans la colonne 'country' est présent dans la liste des équipes
df = df[df['country'].isin(all_teams)]

# Créer une colonne 'non_participant' qui indique si le pays n'est ni dans home_team ni dans away_team
df['non_participant'] = df['country'].apply(lambda x: 1 if x not in all_teams else 0)

# Regrouper par pays et par compétition, puis compter le nombre de fois où le pays est non participant
non_participants = df.groupby(['country', 'tournament'])['non_participant'].sum().reset_index()

# Renommer la colonne 'non_participant' en 'hote'
non_participants = non_participants.rename(columns={'non_participant': 'hote'})

# Supprimer les lignes où 'hote' est égal à 0
non_participants = non_participants[non_participants['hote'] != 0]

# Exporter les données dans un fichier CSV
non_participants.to_csv("non_participants.csv", index=False)
