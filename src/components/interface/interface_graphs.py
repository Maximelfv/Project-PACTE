from dash import Dash, html

from src.components import ids

def render(app: Dash, machine: str) -> html.Div:
    return html.Div(
        id=ids.INTERFACE_GRAPHS,
        className="interface-graph",
        children=[
            html.H4("graph 1"),
            html.H4("graph 2"),
            html.H4("graph 3"),
            #html.Div(
                #children=[
                    #html.H4("graph 4"),
                    #histobar.render(app, ids.MACHINE1)
                #]
           # )
        ]
    )