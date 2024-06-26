import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app

layout = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle(html.Strong("Cadastrar novo Usuário"))),
        dbc.ModalBody(
            [
                dbc.Row(
                    dbc.Col(
                        [
                            dbc.Label(html.Strong("Setor:")),
                            dbc.Select(
                                id="modal-user-sector-select",
                                options=[],
                                placeholder="Selecione um setor",
                            ),
                        ],
                        width=8,
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            dbc.Label(html.Strong("Acesso:")),
                            dbc.Select(
                                id="modal-user-role-select",
                                options=[
                                    {"label": "Administrador", "value": "admin"},
                                    {"label": "Operador", "value": "operator"},
                                ],
                                placeholder="Selecione um nível de acesso",
                            ),
                        ],
                        width=8,
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            dbc.Label(html.Strong("Nome:")),
                            dbc.Input(
                                id="modal-user-name-input",
                                type="text",
                                placeholder="Digite o nome",
                            ),
                        ],
                        width=8,
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        html.P(
                            id="modal-user-error-message",
                            style={"display": "none", "color": "red"},
                        ),
                        width=12,
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            html.Br(),
                            dbc.Button(
                                "Adicionar",
                                color="success",
                                id="modal-user-add-btn",
                                style={"margin-bottom": "20px"},
                            ),
                        ],
                        width=4,
                    )
                ),
            ]
        ),
    ],
    id="modal-user",
    backdrop="static",
    scrollable=True,
)


@app.callback(
    Output("modal-user", "is_open"),
    [
        Input("open-modal-user", "n_clicks"),
        Input("modal-user-add-btn", "n_clicks"),
    ],
    [State("modal-user", "is_open")],
)
def toggle_user_modal(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open
