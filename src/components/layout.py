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

def menu_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-menu",
        children=[
            html.Ul(
                children=[
                    html.Li(
                        children=[
                            html.A(
                                href="Machine_1",
                                children="Machine 1"),
                        ]
                    ),
                    html.Li(
                        children=[
                            html.A(
                                href="Machine_1",
                                children="Machine 1"),
                        ]
                    ),
                    html.Li(
                        children=[
                            html.A(
                                href="Machine_1",
                                children="Machine 1"),
                        ]
                    )
                ]
            )
        ]
    )