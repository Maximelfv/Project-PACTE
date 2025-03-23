from dash import Dash, html

from src.components.layout import body_layout, header_layout
from src.components.teste import teste_section
from src.components import ids

from src.components.callbacks import register_callbacks

from src.components.graph import barre_horizontale, calendrier, camenber, histobar

def main() -> None:
    app = Dash()
    app.title = "Projet PACTE - Tableau de bord"
    app.layout = html.Div(
        id=ids.PROJET_PACTE,
        className= "PACTE-Projet",
        children=[
            header_layout(app),
            body_layout(app),
            teste_section(app),
            histobar.render(app, "Carottage"),
            barre_horizontale.render(app, "Carottage"),
            camenber.render(app, "Carottage"),
            calendrier.render(app, "Carottage"),


        ]
    )

    # Enregistre tous les callbacks
    register_callbacks(app)
    
    app.run_server(debug=True)


if __name__ == "__main__":
    main()