from dash import Output, Input, callback
import dash
from dash import Dash, html

from src.components import ids
from src.components.graph import barre_horizontale, histobar, camember

def register_radiolist_graph_info_callbacks(app: Dash) -> html.Div:
    """Enregistre les callbacks pour les éléments de type RadioItems."""
    @app.callback(
        Output("radio-store", "data"),
        Input("info-radio", "value")
    )
    def graph_info(value: str) -> html.Div:
        """Met à jour le graphique affiché en fonction de la valeur sélectionnée."""
        ctx = dash.callback_context
        if not ctx.triggered:
            return "Taux de production (u/min)"
        
        # ctx.triggered = [{'prop_id': 'info-radio.value'}]
        clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
        return value