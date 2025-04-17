from dash import Dash, html

from src.components import ids
from src.components.calcul.Taux_prod import prod_journaliere, prod_mensuel, prod_annuel, prod_semaine, prod_horaire
from src.components.calcul.Temperature import temp_horaire
from src.components.calcul.Pression import pression_horaire
from src.components.calcul.Conso_elect import conso_elec_horaire

def render(app: Dash, machine: str) -> html.Div:
    return html.Div(
        id=ids.INTERFACE_INFOS_GLOBAL,
        className="interface-global-information",
        children=[
            html.Div([
                html.Div("📈", className="icon"),
                html.H5("Production annuelle"),
                html.P(f"{prod_annuel(machine):,.2f} unités", className="valeur")
            ], className="card"),

            html.Div([
                html.Div("🌡️", className="icon"),
                html.H5("Température actuelle"),
                html.P(f"{temp_horaire(machine):.2f} °C", className="valeur")
            ], className="card"),

            html.Div([
                html.Div("🧪", className="icon"),
                html.H5("Pression actuelle"),
                html.P(f"{pression_horaire(machine):.2f} bar", className="valeur")
            ], className="card"),

            html.Div([
                html.Div("⚡", className="icon"),
                html.H5("Consommation électrique"),
                html.P(f"{conso_elec_horaire(machine):.2f} kWh", className="valeur")
            ], className="card"),
        ]
    )