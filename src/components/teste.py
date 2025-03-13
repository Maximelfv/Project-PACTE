import dash
from dash import Dash, html
from dash.dependencies import Input,Output

from src.components import ids



def teste_section(app: Dash) -> html.Div:   

    @app.callback(
    Output(ids.OUTPUT_TEST, "children"),
    Input(ids.MACHINE1, "n_clicks"),
    Input(ids.MACHINE2, "n_clicks"),
    Input(ids.MACHINE3, "n_clicks")
    )
    def update_image_test(n1: int, n2: int, n3: int) -> html.Img:
        chemin_image = {
        "machine1": "assets/image/image_test/54140107063_61001e472e_o.jpg",
        "machine2": "assets/image/image_test/54140107473_ec923d84e3_o.jpg",
        "machine3": "assets/image/image_test/54140154614_224e5144e3_o.jpg"
        }

        ctx = dash.callback_context  # Permet de voir quel élément a déclenché le callback
        if not ctx.triggered:
            return "Cliquez sur une machine pour voir ses informations."
            #Avant de cliquer sur une machine → ctx.triggered = []
            #Après un clic sur "Machine 1" → ctx.triggered = [{'prop_id': 'machine1.n_clicks'}]

        clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]   #ex: machine1

        return html.Img(
                src=chemin_image.get(clicked_id,"/assets/image/image_test/Logo_stickers.png"),
                alt="teste 1",
                style={"width": "150px", "height": "150px"} 
            )
    
    
    return html.Div(
        id=ids.OUTPUT_TEST,
        
    )






