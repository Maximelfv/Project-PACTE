import dash
from dash.dependencies import Input, Output
from dash import Dash,html

from src.components import ids
from src.components.interface import interface_global_infos,interface_graphs,interface_title

def register_menu_callbacks(app):
    @app.callback(
        Output(ids.INTERFACE_LAYOUT, "children"),
        Input(ids.MACHINE1, "n_clicks"),
        Input(ids.MACHINE2, "n_clicks"),
        Input(ids.MACHINE3, "n_clicks"),         
    )
    def user_info(n1: int, n2: int, n3: int) -> html.Div:
        ctx = dash.callback_context  # Permet de voir quel élément a déclenché le callback
        if not ctx.triggered:
            return "Cliquez sur une machine pour voir ses informations."
            #Avant de cliquer sur une machine → ctx.triggered = []
            #Après un clic sur "Machine 1" → ctx.triggered = [{'prop_id': 'machine1.n_clicks'}]
        
        clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]

        return  [
            interface_title.render(app, clicked_id),
            interface_global_infos.render(app, clicked_id),
            interface_graphs.render(app, clicked_id),  
        ]
