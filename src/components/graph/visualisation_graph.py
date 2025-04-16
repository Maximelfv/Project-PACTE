"""
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Liste des types de graphiques disponibles
graph_options = {
    "📈 Line Chart": "line",
    "📊 Histogram": "histogram",
    "📊 Bar Chart": "bar",
    "📊 Pie Chart": "pie",
    "🌞 Sunburst Chart": "sunburst",
    "🟩 Treemap": "treemap",
    "📉 Boxplot": "box",
    "🎻 Violin Plot": "violin",
    "📊 Cumulative Histogram": "histogram_cumulative",
    "📈 ECDF Plot": "ecdf",
    "🌍 Choropleth Map": "choropleth",
    "📍 Scatter Mapbox": "scatter_mapbox",
    "📍 Bubble Map": "scatter_geo",
    "🕒 Timeline Chart": "timeline",
    "📡 Radar Chart": "radar",
    "🏆 Candlestick Chart": "candlestick"
}

# Layout de l'application
app.layout = html.Div([
    html.H1("Visualisation des Graphiques avec Plotly", style={"textAlign": "center"}),
    dcc.Dropdown(
        id="graph-selector",
        options=[{"label": k, "value": v} for k, v in graph_options.items()],
        value="line",
        clearable=False,
        style={"width": "50%", "margin": "auto"}
    ),
    dcc.Graph(id="graph-output")
])

# Callback pour mettre à jour le graphique
@app.callback(
    Output("graph-output", "figure"),
    Input("graph-selector", "value")
)
def update_graph(graph_type):
    # Chargement de données exemples
    df = px.data.gapminder()
    df_tips = px.data.tips()

    if graph_type == "line":
        fig = px.line(df_tips, x="total_bill", y="tip", title="Line Chart: Pourboires vs Facture")

    elif graph_type == "histogram":
        fig = px.histogram(df_tips, x="total_bill", title="Histogram: Distribution des factures")

    elif graph_type == "bar":
        fig = px.bar(df_tips, x="day", y="total_bill", title="Bar Chart: Factures par jour")

    elif graph_type == "pie":
        fig = px.pie(df_tips, names="day", values="total_bill", title="Pie Chart: Répartition des factures")

    elif graph_type == "sunburst":
        fig = px.sunburst(df, path=["continent", "country"], values="pop", title="Sunburst: Population par continent")

    elif graph_type == "treemap":
        fig = px.treemap(df, path=["continent", "country"], values="pop", title="Treemap: Population par pays")

    elif graph_type == "box":
        fig = px.box(df_tips, x="day", y="total_bill", title="Boxplot: Distribution des factures par jour")

    elif graph_type == "violin":
        fig = px.violin(df_tips, x="day", y="total_bill", title="Violin Plot: Distribution des factures par jour")

    elif graph_type == "histogram_cumulative":
        fig = px.histogram(df_tips, x="total_bill", cumulative=True, title="Histogramme Cumulatif")

    elif graph_type == "ecdf":
        fig = px.ecdf(df_tips, x="total_bill", title="ECDF: Répartition cumulative des factures")

    elif graph_type == "choropleth":
        fig = px.choropleth(df, locations="iso_alpha", color="gdpPercap", title="Choropleth Map: PIB par pays")

    elif graph_type == "scatter_mapbox":
        fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="country", zoom=1,
                                title="Scatter Mapbox: Pays du monde")
        fig.update_layout(mapbox_style="open-street-map")

    elif graph_type == "scatter_geo":
        fig = px.scatter_geo(df, locations="iso_alpha", color="continent", title="Bubble Map: Population par pays")

    elif graph_type == "timeline":
        df_flights = px.data.flights()
        fig = px.timeline(df_flights, x_start="month", x_end="carrier", y="passengers", title="Timeline des vols")

    elif graph_type == "radar":
        df_radar = pd.DataFrame({
            "Critère": ["Qualité", "Prix", "Service", "Innovation", "Fiabilité"],
            "Valeurs": [80, 60, 70, 90, 75]
        })
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=df_radar["Valeurs"],
            theta=df_radar["Critère"],
            fill="toself"
        ))
        fig.update_layout(title="Radar Chart: Évaluation des Critères")

    elif graph_type == "candlestick":
        fig = go.Figure(data=[go.Candlestick(
            x=["2023-01-01", "2023-01-02", "2023-01-03"],
            open=[100, 105, 102],
            high=[110, 115, 108],
            low=[95, 98, 100],
            close=[105, 102, 107]
        )])
        fig.update_layout(title="Candlestick Chart: Données financières")

    else:
        fig = go.Figure()

    return fig


# Exécution de l'application
if __name__ == "__main__":
    app.run_server(debug=True)

"""
