from dash import dcc, html
from dash import Dash

from datetime import datetime

def render(app: Dash, date: datetime) -> html.Div:
    return html.Div(
        className="modern-date-picker-container",
        children=[
            html.Label("🗓️ Sélectionner une date :", className="label"),
            dcc.DatePickerSingle(
                id="custom-date-picker",
                display_format="DD/MM/YYYY",
                placeholder="Choisir une date",
                className="modern-date-picker",
                style={"border": "none"},
                date=date,
            ),
            html.Div(id="selected-date-output", className="date-output")
        ]
    )
