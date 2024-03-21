import pandas as pd

# Données pour le fichier de faits
data_faits = {
    'ID': [1, 2, 3],
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Quantité': [10, 15, 20]
}

# Données pour la première table de dimension
data_dimension1 = {
    'ID': [1, 2, 3],
    'Produit': ['Produit A', 'Produit B', 'Produit C'],
    'Catégorie': ['A', 'B', 'C']
}

# Données pour la deuxième table de dimension
data_dimension2 = {
    'ID': [1, 2, 3],
    'Client': ['Client 1', 'Client 2', 'Client 3'],
    'Ville': ['Ville 1', 'Ville 2', 'Ville 3']
}

# Création des dataframes
df_faits = pd.DataFrame(data_faits)
df_dimension1 = pd.DataFrame(data_dimension1)
df_dimension2 = pd.DataFrame(data_dimension2)

# Export des fichiers CSV
df_faits.to_csv('fichier_faits.csv', index=False)
df_dimension1.to_csv('table_dimension1.csv', index=False)
df_dimension2.to_csv('table_dimension2.csv', index=False)

print("Fichiers exportés avec succès selon le modèle en étoile.")
