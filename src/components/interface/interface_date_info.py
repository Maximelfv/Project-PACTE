from dash import html, dcc
from dash import Dash

from src.components.interface import interface_date_selector, interface_timer_selector

def render(app: Dash, timing: str) -> html.Div:
    return html.Div(
        className="date-infos",
        children=[
            interface_date_selector.render(app),
            interface_timer_selector.render(app, timing),
        ]
    )
