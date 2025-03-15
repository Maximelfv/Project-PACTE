from dash import Dash, html, dcc
import plotly.express as px 

from src.components import ids
from src.components import Lecture_données as ld

def render(app: Dash, machine: str) -> html.Div:
    les_machines = [ids.MACHINE1, ids.MACHINE2, ids.MACHINE3]

    Y = ld.taux_prod(machine)[machine]
    X = ld.date(machine)

    return html.Div(
        className="MachineDropDown",
        children=[
            dcc.Graph(
                    figure=px.bar(X, Y, x="date", y="taux de production", color="yellow", text="machine")
                )
        ]
    )