from dash import Dash, html

from src.components import ids
from src.components.graph import barre_horizontale,camenber,histobar

def render(app: Dash, machine: str) -> html.Div:
    return html.Div(
        id=ids.INTERFACE_GRAPHS,
        className="interface-graph",
        children=[
            barre_horizontale.render(app, machine),
            camenber.render(app, machine),
            histobar.render(app, machine)            
        ]
    )