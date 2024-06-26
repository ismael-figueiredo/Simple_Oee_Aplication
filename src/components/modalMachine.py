import sqlite3
import time

import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import *

layout = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle([html.Strong("Cadastrar nova máquina")])),
        dbc.ModalBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Setor:")]),
                                dbc.Select(
                                    id="modal-machine-sector-select",
                                    options=[],
                                    placeholder="Selecione um setor",
                                ),
                            ],
                            width=8,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label([html.Strong("Máquina:")]),
                                dbc.Input(
                                    id="modal-machine-name-input",
                                    type="text",
                                    placeholder="Digite o nome da máquina",
                                ),
                            ],
                            width=8,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P(
                                    id="modal-machine-error-msg",
                                    style={"display": "none", "color": "red"},
                                ),
                            ],
                            width=12,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Br(),
                                dbc.Button(
                                    "Adicionar",
                                    class_name="btn btn-success btn-lg",
                                    id="modal-machine-add-button",
                                    style={"margin-bottom": "20px"},
                                ),
                            ],
                            width=4,
                        ),
                    ]
                ),
            ]
        ),
    ],
    id="modal-machine",
    backdrop="static",
    scrollable=True,
)


@app.callback(
    Output("modal-machine", "is_open"),
    [
        Input("open-modal-machine", "n_clicks"),
        Input("modal-machine-add-button", "n_clicks"),
    ],
    [State("modal-machine", "is_open")],
)
def toggle_machine_modal(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open
