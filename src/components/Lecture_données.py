import pandas as pd
import sys
import re
from datetime import datetime, timedelta

try:
    df=pd.read_csv("data/Database.csv", sep=";")
except:
    print("Erreur lor de la lecture du fichier")
    sys.exit(1)

#print(df.head())

types_machines=df["Machine"].unique()
#print("Machines détectées:", types_machines)

dico_machines={machine: df[df["Machine"] == machine].to_dict(orient="records") for machine in types_machines}

def type_machines():
    return types_machines

def type_donnees():
    return df.columns.tolist()

def date (machine):
     return df["Horodatage"].str.split(" ").str[0].unique().tolist()

def heure(machine):
     return df["Horodatage"].str.split(" ").str[1].unique().tolist()

def horodatage(machine):
    return [dico["Horodatage"] for dico in dico_machines[machine]]

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



def infos_graph(machine, donnee, timing,date):
    
    
    df_temp = df.copy()
    
    df_temp["Horodatage"] = pd.to_datetime(df_temp["Horodatage"], format="%Y-%m-%d %H:%M")
    df_temp["Année"] = df_temp["Horodatage"].dt.year
    df_temp["Mois"] = df_temp["Horodatage"].dt.month
    df_temp["Jour"] = df_temp["Horodatage"].dt.day
    df_temp["Heure"] = df_temp["Horodatage"].dt.hour

    annee = date.year
    mois = date.month
    jour = date.day

    if timing=="annee":

        filtre = (df_temp["Machine"] == machine) & (df_temp["Année"] == annee)
        df_filtre = df_temp[filtre]
        
        df_groupe = df_filtre.groupby("Mois")[donnee].mean().reset_index()

        return df_groupe

    elif timing=="mois":
        
        filtre = (df_temp["Machine"]== machine)& (df_temp["Année"]==annee) & (df_temp["Mois"]==mois)
        df_filtre = df_temp[filtre]

        df_groupe = df_filtre.groupby("Jour")[donnee].mean().reset_index()

        return df_groupe
    
    elif timing=="jour":
        
        filtre = (df_temp["Machine"]== machine)& (df_temp["Année"]==annee) & (df_temp["Mois"]==mois) & (df_temp["Jour"]==jour)
        df_filtre = df_temp[filtre]

        df_groupe = df_filtre.groupby("Heure")[donnee].mean().reset_index()

        return df_groupe
