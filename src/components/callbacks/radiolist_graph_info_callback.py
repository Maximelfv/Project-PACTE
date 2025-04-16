from dash import Output, Input, callback
import dash
from dash import Dash, html

from src.components import ids
from src.components.graph import barre_horizontale, histobar, camember

def register_radiolist_graph_info_callbacks(app: Dash) -> None:
    """Enregistre les callbacks pour les éléments de type RadioItems."""
    @app.callback(
        Output(ids.INTERFACE_GRAPHS, "children"),
        Input("radio-store", "data"),
        Input("machine-store", "data"),
    )
    def graph_info(value1: str, value2: str) -> html.Div:
        """Met à jour le graphique affiché en fonction de la valeur sélectionnée."""
        ctx = dash.callback_context
        if not ctx.triggered:
            return "Taux de production (u/min)"
        
        # ctx.triggered = [{'prop_id': 'info-radio.value'}]
        clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
        return [
            barre_horizontale.render(app, value2, value1),
            camember.render(app, value2, value1),
            histobar.render(app, value2, value1),
            barre_horizontale.render(app, value2, value1), 
        ]