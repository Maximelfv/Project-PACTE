import pandas as pd
import sys
import re


try:
    df=pd.read_csv("data/Database.csv", sep=";")
except:
    print("Erreur lor de la lecture du fichier")
    sys.exit(1)

#print(df.head())

types_machines=df["Machine"].unique()
#print("Machines détectées:", types_machines)

dico_machines={machine: df[df["Machine"] == machine].to_dict(orient="records") for machine in types_machines}


def date (machine):
     return df["Horodatage"].str.split(" ").str[0].unique().tolist()

def heure(machine):
     return df["Horodatage"].str.split(" ").str[1].unique().tolist()

def taux_prod(machine):
    return [dico["Taux de production (u/min)"] for dico in dico_machines[machine]]

def temperature(machine):
    return [dico["Température (°C)"] for dico in dico_machines[machine]]

def pression(machine):
    return [dico["Pression (bar)"] for dico in dico_machines[machine]]

def defaut(machine, donnée):
    data_machine = dico_machines.get(machine, [])

    resultats = []

    for record in data_machine:
        défaut_info = record.get("Défauts détectés", "")

        match = re.match(r"([a-zA-Z\s]+)\s\((\d+(\.\d+)?)%\)", défaut_info)
        if match:
            if donnée == "type":
                resultats.append(match.group(1).strip()) 
            elif donnée == "nbre":
                resultats.append(float(match.group(2)))

    return resultats

def defauts(machine):
    return [dico ["Défauts détectés"] for dico in dico_machines[machine]]

def energie(machine):
    return [dico["Énergie Consommée (kWh)"] for dico in dico_machines[machine]]


def infos(date, heure, machine, donnee):
    horo_recole=date+" "+heure
    
    filtre = (df["Horodatage"] == horo_recole) & (df["Machine"] == machine)
    resultat = df.loc[filtre, donnee]

    if not resultat.empty:
        return resultat.values[0]
    else:
        return "No data available"



print (infos("2024-03-01", "09:35", "Carottage", "Température (°C)"))