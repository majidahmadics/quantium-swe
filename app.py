from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv("df_final.csv")

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Sales over time",
    labels={"sales": "Sales", "date": "Date"}
)

app.layout = html.Div(children=[
    html.H1(children='Soul Foods Sales Dashboard'),

    html.Div(children='''
        Soul Foods's sales over time for pink Morsels
    '''),

    dcc.Graph(
        id='sales-date-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)