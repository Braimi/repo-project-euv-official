import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Configuration
seed_value = 42
max_votes = 1000
country_code = "ES"  # 🇪🇸 Espagne uniquement
output_folder = "../stockage_resultat"
output_file = "script_votes_du_public_es.txt"

# Pour reproductibilité
np.random.seed(seed_value)
random.seed(seed_value)

# Format de numéro pour l'Espagne
def generate_spanish_mobile_number():
    return "+34 6{0:01d} {1:02d} {2:02d} {3:02d}".format(
        random.randint(0, 9),
        random.randint(0, 99),
        random.randint(0, 99),
        random.randint(0, 99)
    )

# Générer les données
data = {
    "COUNTRY CODE": [],
    "MOBILE NUMBER": [],
    "SONG NUMBER": [],
    "TIMESTAMP": []
}

now = datetime.now()

for _ in range(max_votes):
    data["COUNTRY CODE"].append(country_code)
    data["MOBILE NUMBER"].append(generate_spanish_mobile_number())
    data["SONG NUMBER"].append(random.randint(1, 25))
    sec = random.randint(0, 3600)
    time = now - timedelta(seconds=sec)
    data["TIMESTAMP"].append(time.strftime('%Y-%m-%dT%H:%M:%S'))

# Créer le DataFrame
df = pd.DataFrame(data)

# Créer le dossier s’il n’existe pas
os.makedirs(output_folder, exist_ok=True)

# Enregistrer le fichier
output_path = os.path.join(output_folder, output_file)
df.to_csv(output_path, index=False, header=False)

print(f"✅ Fichier enregistré : {output_path}")

