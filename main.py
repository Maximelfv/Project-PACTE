from dash import Dash, html
from dash import dcc

from src.components.layout import body_layout, header_layout
from src.components import ids

from src.components.callbacks import register_callbacks

from src.components.calcul.today_informations import today_test

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
    
    app.run_server(debug=True)


if __name__ == "__main__":
    main()