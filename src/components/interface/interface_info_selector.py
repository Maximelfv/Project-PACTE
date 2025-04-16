from dash import html, dcc
from dash import Dash

def render(app: Dash) -> html.Div:
    return html.Div(
        className="info-selector",
        children=[
            html.Label("📊 Type d'information à afficher :", className="label"),
            dcc.RadioItems(
                id="info-radio",
                options=[
                    {"label": "⚙️ Production", "value": "prod"},
                    {"label": "🌡️ Température", "value": "temp"},
                    {"label": "⚡ Consommation", "value": "conso"},
                    {"label": "📈 Pression", "value": "pression"},
                    {"label": "🚨 Défauts", "value": "defauts"},
                ],
                value="prod",
                labelStyle={"display": "flex", "align-items": "center"},
                className="radio"
            ),
            html.Div(id="info-output", className="radio-output")
        ]
    )
