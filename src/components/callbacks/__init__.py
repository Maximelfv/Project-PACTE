from dash import Dash
from src.components.callbacks import menu_callback
from src.components.callbacks import radiolist_graph_info_callback


def register_callbacks(app: Dash) -> None:
    menu_callback.register_menu_callbacks(app)
    radiolist_graph_info_callback.register_radiolist_graph_info_callbacks(app)
    