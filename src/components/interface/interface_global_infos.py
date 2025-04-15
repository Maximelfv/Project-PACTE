from dash import Dash, html

from src.components import ids
from src.components.calcul.Taux_prod import prod_journaliere, prod_mensuel, prod_annuel, prod_semaine

def render(app: Dash, machine: str) -> html.Div:
    return html.Div(
        id=ids.INTERFACE_INFOS_GLOBAL,
        className="interface-global-information",
        children=[
            html.H4(f"Voici la productuion annuelle de {machine}\n        {prod_annuel(machine)    }"),
            html.H4(f"infos {machine} 2"),
            html.H4(f"infos {machine} 3"),
            html.H4(f"infos {machine} 4"),
        ]
    )