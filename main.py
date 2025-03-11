from dash import Dash, html

from src.components.layout import body_layout, header_layout
from src.components.teste import teste_section

def main() -> None:
    app = Dash()
    app.title = "Projet PACTE - Tableau de bord"
    app.layout = html.Div(
        className= "PACTE-Projet",
        children=[
            header_layout(app),
            body_layout(app),
            teste_section(app),
        ]
    )
    """"
    app.layout = html.Header(
        className="Body",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                children=[
                    menu_layout(app),
                    app_div_layout(app)
                ]
                
            )
        ]
    )
    """
    app.run()


if __name__ == "__main__":
    main()