from dash import Dash, html, dcc
import plotly.express as px 

from . import machine_dropdown
from src.components import ids

def header_layout(app: Dash) -> html.Header:
    return html.Header(
        className="app-header",
        children=[
            html.H1(app.title),
            html.Img(src="assets/image/logo_HESTIM.png", alt="logo_hestim"),
            html.Hr()
        ]
    )



def body_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-body",
        children=[
            menu_layout(app),
            interface_layout(app),
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
                            html.Span(
                                id=ids.MACHINE1,
                                n_clicks=0,
                                children="Machine 1"),
                        ]
                    ),
                    html.Li(
                        children=[
                            html.Span(
                                id=ids.MACHINE2,
                                n_clicks=0,
                                children="Machine 2"),
                        ]
                    ),
                    html.Li(
                        children=[
                            html.Span(
                                id=ids.MACHINE3,
                                n_clicks=0,
                                children="Machine 3"),
                        ]
                    )
                ]
            )
        ]
    )



def interface_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-interface",
        children=[
            interface_title(app),
            interface_global_information(app),
            interface_graph(app),
            
        ]
    )


def interface_title(app: Dash) -> html.Div:
    return html.Div(
        className="interface-title",
        children=[
            html.H3("teste interface titre")
        ]
    )


def interface_global_information(app: Dash) -> html.Div:
    return html.Div(
        className="interface-global-information",
        children=[
            html.H4("infos 1"),
            html.H4("infos 2"),
            html.H4("infos 3"),
            html.H4("infos 4"),
        ]
    )

def interface_graph(app: Dash) -> html.Div:
    return html.Div(
        className="interface-graph",
        children=[
            html.H4("graph 1"),
            html.H4("graph 2"),
            html.H4("graph 3"),
            html.Div(
                children=[
                    html.H4("graph 4"),
                    dcc.Graph(
                        figure=px.bar(px.data.medals_long(), x="medal", y="count", color="nation", text="nation")
                    )
                ]
            )
        ]
    )