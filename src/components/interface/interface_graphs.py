from dash import Dash, html

from src.components import ids
from src.components.graph import barre_horizontale,histobar,camember
from datetime import datetime

def render(app: Dash, machine: str, donnee: str, timing: str, date: datetime) -> html.Div:
    return html.Div(
        id=ids.INTERFACE_GRAPHS,
        className="interface-graph",
        children=[
            barre_horizontale.render(app, machine, donnee, timing, date),
            camember.render(app, machine, donnee, timing, date),
            histobar.render(app, machine, donnee, timing, date),
            barre_horizontale.render(app, machine, donnee, timing, date),          
        ]
    )