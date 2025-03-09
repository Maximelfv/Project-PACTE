import dash
from dash import dcc, html

# Création de l'application Dash
app = dash.Dash(__name__)

# Définition du layout
app.layout = html.Div([
    html.H1("Bonjour, Dash !"),
    
])

# Lancer l'application
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  # use_reloader=False pour éviter l'iframe dans Spyder
