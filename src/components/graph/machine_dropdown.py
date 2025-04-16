from dash import Dash, html, dcc

def render(app: Dash) -> html.Div:
    les_machines = ["machine1", "machine2", "machine3"]

    return html.Div(
        className="MachineDropDown",
        children=[
            html.H6("Choix des machines"),
            dcc.Dropdown(
                options = [{"label": machine, "value": machine} for machine in les_machines],
                value= les_machines,
                multi=True,
            ),
        ]
    )