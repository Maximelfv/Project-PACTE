from dash import Output, Input, callback
import dash
from dash import Dash, html

from src.components import ids
from src.components.interface import interface_date_info, interface_global_infos, interface_info_selector, interface_graphs, interface_title
from datetime import datetime

def register_mise_a_jour_graph_callbacks(app: Dash) -> tuple[str, html.Div]:
    """Enregistre les callbacks pour les éléments de type RadioItems."""
    @app.callback(
        Output(ids.INTERFACE_LAYOUT, "children"),
        Input("machine-store", "data"),
        Input("radio-store", "data"),
        Input("timing-store", "data"),
        Input("date-store", "data"),
    )
    def graph_page(machine: str, donnee: str, timing: str, date: datetime) -> html.Div:
        """Met à jour le graphique affiché en fonction de la valeur sélectionnée."""
        ctx = dash.callback_context
        if not ctx.triggered:
            return ""
        
        # ctx.triggered = [{'prop_id': 'info-radio.value'}]
        clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]

        date = datetime.strptime(date, "%Y-%m-%d")
        
        return [
            interface_title.render(app, machine),
            interface_date_info.render(app),
            interface_global_infos.render(app, machine),
            interface_info_selector.render(app),
            interface_graphs.render(app, machine, donnee, timing, date),
        ]