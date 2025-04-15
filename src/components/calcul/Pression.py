""" A SUPRIMMER APRES TESTE """

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

""" ----------------------------------------------"""


from datetime import datetime
import numpy as np

from src.components import Lecture_données as ld
from src.components.calcul.today_informations import today, today_test, hour, hour_test, month, month_test, year, year_test, start_of_week, start_of_week_test

def pression_horaire(machine: str) -> int:
    data = ld.dico_machines[machine]
    total = []

    for ligne in data:
        date_i = datetime.strptime(ligne["Horodatage"], "%Y-%m-%d %H:%M")
        if date_i.date() == today_test and date_i.hour== hour_test:
            total.append(ligne["Pression (bar)"])

    print(f"Pression horaire pour {machine} le {today_test} à {hour_test} : {np.mean(total):.2f} bar")
    return np.mean(total)

print(pression_horaire("Carottage"))