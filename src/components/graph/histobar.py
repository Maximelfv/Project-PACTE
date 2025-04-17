from dash import Dash, html, dcc
import plotly.express as px 

import pandas as pd
from datetime import datetime

from src.components import ids
from src.components import Lecture_données as ld

def render(app: Dash, machine: str, donnee: str, timing: str, date: datetime) -> dcc.Graph:
    df_graph = ld.infos_graph(machine, donnee, timing, date)

    X = df_graph.iloc[:, 0] 
    Y = df_graph.iloc[:, 1] 


   

    df = pd.DataFrame({
        "label": X,
        "valeur": Y
    })


    fig = px.bar(
        df,
        x="label",
        y="valeur",
        title=f"{donnee} - {machine}")

    fig.update_traces(
        texttemplate='%{y}',
        textposition='outside',
        marker_color='orange'
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        plot_bgcolor="#f9f9f9",
        margin={"t": 30, "b": 30, "l": 40, "r": 10}
    )

    return html.Div(
        className="histobar",
        children=dcc.Graph(
            figure=fig,
            style={"width": "400px", "height": "400px"}
        )
    )