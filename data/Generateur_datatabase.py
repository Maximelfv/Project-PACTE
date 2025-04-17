# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 18:13:27 2025

@author: thomas.leroy
"""

import pandas as pd
import random
from datetime import datetime, timedelta
 
# Définition des paramètres
machines = ["Soufflage", "Carottage", "Remplissage", "Étiquetage"]
defauts_possibles = ["Bulles d'air (2%)", "Déformation (1%)", "Fuites (1.5%)",
                     "Rayures (1%)", "Mauvais alignement (0.8%)", "Aucun"]
 
# Définition de l'heure de départ
start_time = datetime(2024, 3, 1, 8, 0)
 
# Génération des 1000 lignes de données
data_rows = []
for i in range(3000):
    horodatage = start_time + timedelta(minutes=5 * i)  # Incrémentation de 5 minutes
    machine = random.choice(machines)
    taux_production = random.randint(100, 150)  # Unités/min
    if machine=="Soufflage":
        temperature = round(random.uniform(100.0, 200.0), 1)  # °C
        pression = round(random.uniform(4.5, 8.5), 1)  # bar
    else:
        temperature = round(random.uniform(4.5, 7.5), 1)  # °C
        pression = 1  # bar

    defauts = random.choice(defauts_possibles)
    energie = round(random.uniform(1.0, 3.0), 2)  # kWh
 
    data_rows.append([horodatage.strftime("%Y-%m-%d %H:%M"), machine, taux_production,
                      temperature, pression, defauts, energie])
 
# Création du DataFrame
df = pd.DataFrame(data_rows, columns=["Horodatage", "Machine", "Taux de production (u/min)", 
                                      "Température (°C)", "Pression (bar)", "Défauts détectés", 
                                      "Énergie Consommée (kWh)"])
 
# Sauvegarde dans un fichier CSV
file_name = "tableau_production_1000.csv"
df.to_csv(file_name, index=False, sep=";")