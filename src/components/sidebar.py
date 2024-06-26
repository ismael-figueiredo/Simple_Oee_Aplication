import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from flask_login import logout_user

from app import *

layout = dbc.Card(
    [
        html.Div(id="div-ghost"),
        html.Img(
            src="/assets/logo.png",
            className="align-self-center",
            style={
                "width": "150px",
                "height": "150px",
            },
        ),
        html.P(
            "Simplicity MES App",
            className="text-center",
        ),
        html.Hr(),
        dbc.Nav(
            [
                html.H6("Gráficos"),
                dbc.NavLink("Dashboard", href="/dashboard", active="partial"),
                dbc.NavLink("Time-line", href="/timeline", active="partial"),
                html.Hr(),
                html.H6("Cadastros gerais"),
                dbc.NavLink("Usuários", id="open-modal-user", active="partial"),
                dbc.NavLink("Setores", id="open-modal-sector", active="partial"),
                dbc.NavLink("Máquinas", id="open-modal-machine", active="partial"),
                dbc.NavLink(
                    "Tempos",
                    id="open-modal-time",
                    active="partial",
                ),
                html.Hr(),
                html.H6("Cadastro de motivos"),
                dbc.NavLink("Parada", id="open-modal-reason-stop", active="partial"),
                dbc.NavLink(
                    "Não conformidade",
                    id="open-modal-reason-unconform",
                    active="partial",
                ),
                html.Hr(),
                dbc.NavLink("sair", id="logout", href="/login", active="partial"),
            ],
            vertical=True,
            pills=True,
            id="nav_buttons",
            style={"margin-left": "1rem", "margin-right": "1rem"},
        ),
    ],
    style={"width": "100%", "margin-top": "8px"},
)


@app.callback(Output("div-ghost", "children"), [Input("logout", "n_clicks")])
def logout(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    logout_user()
    return ""
