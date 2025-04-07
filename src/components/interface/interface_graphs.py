from dash import Dash, html

from src.components import ids
from src.components.graph import barre_horizontale,histobar,camember

def render(app: Dash, machine: str) -> html.Div:
    return html.Div(
        id=ids.INTERFACE_GRAPHS,
        className="interface-graph",
        children=[
            barre_horizontale.render(app, machine),
            camember.render(app, machine),
            histobar.render(app, machine),
            barre_horizontale.render(app, machine),          
        ]
    )