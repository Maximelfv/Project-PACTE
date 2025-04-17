from dash import Dash
from src.components.callbacks import menu_callback
from src.components.callbacks import radiolist_graph_info_callback
from src.components.callbacks import mise_a_jour_graph_callback
from src.components.callbacks import calendrier_callback
from src.components.callbacks import timing_callback


def register_callbacks(app: Dash) -> None:
    menu_callback.register_menu_callbacks(app)
    radiolist_graph_info_callback.register_radiolist_graph_info_callbacks(app)
    mise_a_jour_graph_callback.register_mise_a_jour_graph_callbacks(app)
    calendrier_callback.register_calendrier_callbacks(app)
    timing_callback.register_timing_callbacks(app)
    