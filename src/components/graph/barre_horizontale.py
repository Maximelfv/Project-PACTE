from dash import Dash, html, dcc
import plotly.express as px 
import pandas as pd
from datetime import datetime

from src.components import ids
from src.components import Lecture_données as ld

def render(app: Dash, machine: str, donnee: str, timing: str, date: datetime) -> html.Div:
    df_graph = ld.infos_graph(machine, donnee, timing, date)

   

    df = pd.DataFrame({
        "Date": df_graph.iloc[:, 0],      
        "Donnee": df_graph.iloc[:, 1]     
    })
  

    
    fig = px.bar(
        df,
        x="Donnee",
        y="Date",
        orientation="h",
        title=f"{donnee} - {machine}"
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
        xaxis_title=donnee,
        yaxis_title="",
        margin={"t": 10, "b": 30, "l": 60, "r": 10},
        height=350
    )
    

    return html.Div(
        className="graph-card",
        children=[
            html.Div(f"📊 {donnee} sur {machine}", className="card-title"),
            dcc.Graph(
                figure=fig,
                config={"displayModeBar": False},  # retire la barre plotly en haut à droite
                className="graph-container"
            )
        ]
    )
        

    

    