from src.components.callbacks import menu_callback


def register_callbacks(app):
    menu_callback.register_menu_callbacks(app)
    