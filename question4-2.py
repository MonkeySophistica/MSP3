import pandas as pd

# Lire le fichier CSV généré précédemment
df = pd.read_csv("question4.csv")

# Obtenir l'entrée avec le plus grand nombre de victoires par époque
idx = df.groupby('epoque')['nombre_de_victoires'].idxmax()
victoires_max_par_epoque = df.loc[idx]

# Écrire le résultat dans un nouveau fichier CSV
victoires_max_par_epoque.to_csv("question4gagnants.csv", index=False)
