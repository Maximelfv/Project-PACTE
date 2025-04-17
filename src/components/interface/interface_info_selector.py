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
                    {"label": "⚙️ Production", "value": "Taux de production (u/min)"},
                    {"label": "🌡️ Température", "value": "Température (°C)"},
                    {"label": "⚡ Consommation", "value": "Énergie Consommée (kWh)"},
                    {"label": "📈 Pression", "value": "Pression (bar)"},
                ],
                value="prod",
                labelStyle={"display": "flex", "align-items": "center"},
                className="radio"
            ),
            html.Div(id="info-output", className="radio-output")
        ]
    )
