from dash import Dash, html
from dash import dcc
import webbrowser
from threading import Timer

from src.components.layout import body_layout, header_layout
from src.components import ids

from src.components.callbacks import register_callbacks

from src.components.calcul.today_informations import today_test

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

def main() -> None:
    app = Dash()
    app.title = "Projet PACTE - Tableau de bord"
    app.layout = html.Div(
        id=ids.PROJET_PACTE,
        className= "PACTE-Projet",
        children=[
            dcc.Store(id="machine-store", data=ids.MACHINE1),
            dcc.Store(id="radio-store", data="Taux de production (u/min)"),
            dcc.Store(id="timing-store", data="mois"),
            dcc.Store(id="date-store", data=str(today_test)),
            header_layout(app),
            body_layout(app),           
        ]
    )

    # Enregistre tous les callbacks
    
    register_callbacks(app)

    Timer(1, open_browser).start()  # attend 1 seconde avant d'ouvrir

    
    app.run_server(debug=True, use_reloader=False)




if __name__ == "__main__":
    main()






