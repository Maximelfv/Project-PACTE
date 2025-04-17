from dash import Output, Input, callback
import dash
from dash import Dash, html

from src.components import ids
from src.components.graph import barre_horizontale, histobar, camember

def register_timing_callbacks(app: Dash) -> html.Div:
    """Enregistre les callbacks pour les éléments de type RadioItems."""
    @app.callback(
        Output("timing-store", "data"),
        Input("periode-radio", "value"),
    )
    def timing_info(value: str) -> None:
        """Met à jour le graphique affiché en fonction de la valeur sélectionnée."""
        ctx = dash.callback_context
        if not ctx.triggered:
            return "mois"
        
        # ctx.triggered = [{'prop_id': 'info-radio.value'}]
        clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
        return value[0]