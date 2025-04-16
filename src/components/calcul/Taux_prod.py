""" A SUPRIMMER APRES TESTE """

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

""" ----------------------------------------------"""

from datetime import datetime

from src.components import Lecture_données as ld
from src.components.calcul.today_informations import today, today_test, hour, hour_test, month, month_test, year, year_test, start_of_week, start_of_week_test

print(month_test)
print(year_test)

def prod_journaliere(machine: str) -> int:
    data = ld.dico_machines[machine]
    total = 0

    for ligne in data:
        date_i = datetime.strptime(ligne["Horodatage"], "%Y-%m-%d %H:%M").date()
        if date_i == today_test:
            total += ligne["Taux de production (u/min)"]

    print(f"Production journalière pour {machine} le {today_test} : {total}")
    return total

def prod_mensuel(machine: str) -> int:
    data = ld.dico_machines[machine]
    total = 0

    for ligne in data:
        date_i = datetime.strptime(ligne["Horodatage"], "%Y-%m-%d %H:%M").date()
        if date_i.year == year_test and date_i.month == month_test:
            total += ligne["Taux de production (u/min)"]

    print(f"Production mensuel pour {machine} durant le mois de {year_test}-{month_test} : {total}")
    return total

def prod_annuel(machine: str) -> int:
    data = ld.dico_machines[machine]
    total = 0

    for ligne in data:
        date_i = datetime.strptime(ligne["Horodatage"], "%Y-%m-%d %H:%M").date()
        if date_i.year == year_test:
            total += ligne["Taux de production (u/min)"]

    print(f"Production annuel pour {machine} durant l'année {year_test} : {total}")
    return total

def prod_semaine(machine: str) -> int:
    data = ld.dico_machines[machine]
    total = 0

    for ligne in data:
        date_i = datetime.strptime(ligne["Horodatage"], "%Y-%m-%d %H:%M").date()
        if start_of_week <= date_i <= today_test:
            total += ligne["Taux de production (u/min)"]

    print(f"Production hebdomadaire pour {machine} du {start_of_week} au {today_test} : {total}")
    return total

def prod_horaire(machine: str) -> int:
    data = ld.dico_machines[machine]
    total = 0

    for ligne in data:
        date_time = datetime.strptime(ligne["Horodatage"], "%Y-%m-%d %H:%M")
        if date_time.date() == today_test and date_time.hour == hour_test:
            total += ligne["Taux de production (u/min)"]

    print(f"Production horaire pour {machine} le {today_test} à {hour_test}h est de: {total}")
    return total

# ✅ Tests
print(prod_journaliere('Carottage'))
print(prod_mensuel('Carottage'))
print(prod_annuel('Carottage'))
print(prod_semaine('Carottage'))
print(prod_horaire('Carottage'))




















