from dash import Dash, html, dcc
import plotly.express as px

from .graph import histobar
from src.components import ids
from src.components.interface import interface_title,interface_global_infos, interface_graphs, interface_date_info, interface_info_selector

def header_layout(app: Dash) -> html.Header:
    return html.Header(
        id=ids.APP_HEADER,
        className="app-header",
        children=[
            html.H1(app.title),
            html.Img(src="assets/image/logo_HESTIM.png", alt="logo_hestim"),
            html.Hr()
        ]
    )



def body_layout(app: Dash) -> html.Div:
    return html.Div(
        id=ids.APP_BODY,
        className="app-body",
        children=[
            menu_layout(app),
            interface_layout(app),
        ]
    )



def menu_layout(app: Dash) -> html.Div:
    return html.Div(
        id=ids.APP_MENU,
        className="app-menu",
        children=[
            html.Ul(
                children=[
                    html.Li(
                        children=[
                            html.Span(
                                ids.MACHINE1,
                                id=ids.MACHINE1,
                                n_clicks=0,
                                ),
                        ]
                    ),
                    html.Li(
                        children=[
                            html.Span(
                                ids.MACHINE2,
                                id=ids.MACHINE2,
                                n_clicks=0,
                                ),
                        ]
                    ),
                    html.Li(
                        children=[
                            html.Span(
                                ids.MACHINE3,
                                id=ids.MACHINE3,
                                n_clicks=0,
                                ),
                        ]
                    ),
                    html.Li(
                        children=[
                            html.Span(
                                ids.MACHINE4,
                                id=ids.MACHINE4,
                                n_clicks=0,
                                ),
                        ]
                    )
                ]
            )
        ]
    )



def interface_layout(app: Dash) -> html.Div:
    return html.Div(
        id=ids.INTERFACE_LAYOUT,
        className="app-interface",
        children=[
            interface_title.render(app, "Remplissage"),
            interface_date_info.render(app),
            interface_global_infos.render(app, "Remplissage"),
            interface_info_selector.render(app),
            interface_graphs.render(app, "Remplissage"),
            
        ]
    )







