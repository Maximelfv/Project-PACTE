from dash import Dash, html

from src.components import ids

def render(app: Dash, machine: str) -> html.Div:
    return html.Div(
        id=ids.INTERFACE_INFOS_GLOBAL,
        className="interface-global-information",
        children=[
            html.H4(f"infos {machine} 1"),
            html.H4(f"infos {machine} 2"),
            html.H4(f"infos {machine} 3"),
            html.H4(f"infos {machine} 4"),
        ]
    )