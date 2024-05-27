import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output

from app import *
from src.components import dashboard, sidebar


def render_layout():
    layout = dbc.Container(
        children=[
            dbc.Row(
                [
                    dbc.Col([sidebar.layout], md=2),
                    dbc.Col(
                        [html.Div(id="adm-content", children=[])],
                        md=10,
                    ),
                ]
            ),
        ],
        fluid=True,
        className="dbc",
    )

    return layout


@app.callback(Output("adm-content", "children"), [Input("base-url", "pathname")])
def render_adm_content(pathname):
    if pathname == "/":
        return dashboard.layout
    if pathname == "/adm":
        return dashboard.layout
    if pathname == "/dashboard":
        return dashboard.layout