from dash import Dash, html

from . import machine_dropdown

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                children=[
                    machine_dropdown.render(app),
                ]
            )
        ]
    )