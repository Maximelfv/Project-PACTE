from dash import html, dcc
from dash import Dash

def render(app: Dash, timing: str) -> html.Div:
    return html.Div(
        className="time-selector",
        children=[
            html.Label("🕐 Période à afficher :", className="label"),
            dcc.RadioItems(
                id="periode-radio",
                options=[
                    {"label": "📆 Journée", "value": "jour"},
                    {"label": "🗓️ Mois", "value": "mois"},
                    {"label": "🗓️ Année", "value": "annee"},
                ],
                value=timing,  # Valeur par défaut
                labelStyle={"display": "block"},
                className="radio"
            ),
            html.Div(id="periode-output", className="radio-output")
        ]
    )

