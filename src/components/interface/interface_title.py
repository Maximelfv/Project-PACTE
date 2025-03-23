from dash import Dash, html

from src.components import ids

def render(app: Dash, machine: str) -> html.Div:
    return html.Div(
        id=ids.INTERFACE_TITLE,
        className="interface-title",
        children=[
            html.H3(machine)
        ]
    )