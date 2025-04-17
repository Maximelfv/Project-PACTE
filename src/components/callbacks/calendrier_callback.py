from dash import Output, Input, callback
import dash
from dash import Dash, html

from src.components import ids
from src.components.interface import interface_date_info, interface_global_infos, interface_info_selector, interface_graphs, interface_title

def register_calendrier_callbacks(app: Dash) -> str:
    """Enregistre les callbacks pour les éléments de type RadioItems."""
    @app.callback(
        Output("date-store", "data"),
        Input("custom-date-picker", "value"),
    )
    def calendrier_info(value: str) -> html.Div:
        """Met à jour le graphique affiché en fonction de la valeur sélectionnée."""
        ctx = dash.callback_context
        if not ctx.triggered:
            return ""
        
        # ctx.triggered = [{'prop_id': 'info-radio.value'}]
        clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
        return value