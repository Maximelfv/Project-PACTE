from dash import Dash, html, dcc
import plotly.express as px 

from dash.dependencies import Input, Output
import calendar
import datetime

from src.components import ids
from src.components import Lecture_données as ld

def render(app: Dash, machine: str) -> html.Div:
    # Liste des mois en français
    mois_noms = ["JANV", "FÉVR", "MARS", "AVR", "MAI", "JUIN", "JUIL", "AOÛT", "SEPT", "OCT", "NOV", "DÉC"]


    # Callback pour mettre à jour les jours du mois sélectionné
    @app.callback(
        Output("calendar-container", "children"),
        Input("mois-slider", "value")
    )
    def update_calendar(mois_selectionne):
        # Nombre de jours dans le mois sélectionné
        jours = list(range(1, calendar.monthrange(2024, mois_selectionne)[1] + 1))

        # Création des boutons pour chaque jour
        jours_buttons = [
            html.Button(str(j), className="day-button", id=f"day-{j}")
            for j in jours
        ]

        return jours_buttons

    # Conteneur des jours du mois
    return html.Div(
        className="MachineDropDown",
        children=[
            # Sélecteur du mois
            dcc.Slider(
                id="mois-slider",
                min=1,
                max=12,
                step=1,
                marks={i+1: mois_noms[i] for i in range(12)},
                value=datetime.datetime.today().month,  # Mois actuel par défaut
            ),
            html.Div(
                id="calendar-container", 
                className="calendar-grid",
            )
        ]
    )



