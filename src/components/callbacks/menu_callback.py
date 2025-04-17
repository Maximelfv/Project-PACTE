import dash
from dash.dependencies import Input, Output
from dash import Dash,html

from src.components import ids
from src.components.interface import interface_global_infos,interface_graphs,interface_title, interface_info_selector, interface_date_info

def register_menu_callbacks(app: Dash):
    @app.callback(
        Output("machine-store", "data"),
        Input(ids.MACHINE1, "n_clicks"),
        Input(ids.MACHINE2, "n_clicks"),
        Input(ids.MACHINE3, "n_clicks"), 
        Input(ids.MACHINE4, "n_clicks"),        
    )
    def user_info(n1: int, n2: int, n3: int, n4:int) -> None:
        ctx = dash.callback_context  # Permet de voir quel élément a déclenché le callback
        if not ctx.triggered:
            return ids.MACHINE1
            #Avant de cliquer sur une machine → ctx.triggered = []
            #Après un clic sur "Machine 1" → ctx.triggered = [{'prop_id': 'machine1.n_clicks'}]
        
        clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]

        return clicked_id
