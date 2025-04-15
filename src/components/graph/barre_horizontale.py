from dash import Dash, html, dcc
import plotly.express as px 
import pandas as pd

from src.components import ids
from src.components import Lecture_données as ld

def render(app: Dash, machine: str) -> html.Div:
    
    Y = ld.taux_prod(machine)
    X = ld.date(machine)

    l = min(len(X),len(Y))

    X,Y=X[:l],Y[:l]

    df=pd.DataFrame({
        "Date":X,
        "Taux de production":Y
        })
    
    fig = px.bar(
        df,
        x="Taux de production",
        y="Date",
        orientation="h",
        title=f"Taux de production - {machine}"
    )
    fig.update_traces(
        texttemplate='%{x}',
        textposition='outside',
        marker_color='orange'
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        plot_bgcolor="#f9f9f9",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Taux (u/min)",
        yaxis_title="",
        margin={"t": 10, "b": 30, "l": 60, "r": 10},
        height=350
    )
    

    return html.Div(
        className="graph-card",
        children=[
            html.Div("📊 Taux de production", className="card-title"),
            dcc.Graph(
                figure=fig,
                config={"displayModeBar": False},  # retire la barre plotly en haut à droite
                className="graph-container"
            )
        ]
    )
        

    

    