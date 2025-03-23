from dash import Dash, html, dcc
import plotly.express as px 

import pandas as pd

from src.components import ids
from src.components import Lecture_données as ld

def render(app: Dash, machine: str) -> html.Div:
    les_machines = [ids.MACHINE1, ids.MACHINE2, ids.MACHINE3]

    Y = ld.taux_prod(machine)
    X = ld.date(machine)

    l = min(len(X),min(Y))

    X,Y=X[:l],Y[:l]

    df=pd.DataFrame({"date":X, "taux de production":Y})


    return html.Div(
        className="MachineDropDown",
        children=[
            dcc.Graph(
                    figure=px.pie(df, names="date", values="taux de production"),
                    style={"width": "300px", "height": "300px"} 

                )
        ]
    )