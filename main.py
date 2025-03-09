from dash import Dash, html

from src.components.layout import create_layout,menu_layout

def main() -> None:
    app = Dash()
    app.title = "Medal"
    app.layout = html.Div(
        className="Body",
        children=[
            menu_layout(app),
            create_layout(app)
        ]
    )
    app.run()


if __name__ == "__main__":
    main()