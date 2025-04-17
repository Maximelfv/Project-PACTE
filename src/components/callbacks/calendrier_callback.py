from dash import Output, Input, callback
import dash
from dash import Dash, html

from src.components import ids
from src.components.interface import interface_date_info, interface_global_infos, interface_info_selector, interface_graphs, interface_title
from datetime import datetime
from src.components.calcul.today_informations import today_test

def register_calendrier_callbacks(app: Dash) -> str:
    """Enregistre les callbacks pour les éléments de type RadioItems."""
    @app.callback(
        Output("date-store", "data"),
        Input("custom-date-picker", "date"),
    )
    def calendrier_info(value) -> str:
        if not value or not isinstance(value, str):
            return str(today_test)  # Valeur par défaut si rien n’est sélectionné

        try:
            date = datetime.fromisoformat(value).date()
            return str(date)
        except ValueError:
            return str(today_test)