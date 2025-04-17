from dash import html, dcc
from dash import Dash

from src.components.interface import interface_date_selector, interface_timer_selector
from datetime import datetime


def render(app: Dash, timing: str, date: datetime) -> html.Div:
    return html.Div(
        className="date-infos",
        children=[
            interface_date_selector.render(app, date),
            interface_timer_selector.render(app, timing),
        ]
    )
