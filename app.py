import os
import pandas as pd
import figures as dv

import plotly.express as px
import dash_bootstrap_components as dbc
import dash_bootstrap_templates as dbt

from dash import Dash, dcc, html
from dash.dependencies import Input, Output


# Text field
def init_text_field(value: str, reference: str):
    """
    Creates a 'dbc' card-component and inserts the text into it
    :param value: text to be displayed
    :param reference: reference of the corresponding UI component
    :return: text-field UI component
    """
    return html.Div(
        [
            dbc.Card(
                dbc.CardBody([
                    html.Div([
                        html.A(
                            html.H3(value),
                            className="list-group-item list-group-item-action",
                            href=reference,
                        )
                    ], style={'textAlign': 'center'})
                ], style={'background-color': '#E8EAF6'})
            ),
        ]
    )


# Figure Card
def init_figure(id: str, plot: str):
    """
    Creates a 'dbc' card-component and inserts the figure into it
    :param id: component ID
    :param plot: plot to be drawn
    :return: figure UI Component
    """
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id=id,
                    figure=plot,
                )
            ])
        ),
    ])


# Initialize the app & building components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Theme Switcher
default_theme = "zephyr"
dark_theme = "vapor"
theme_switcher = dbt.ThemeSwitchAIO(
    aio_id="theme",
    themes=[dbc.themes.BOOTSTRAP, dbc.themes.SLATE]
)

# Dataset
df = pd.read_csv(os.path.join("assets", "cleaned_fifa21_male2.csv"))

# Plots and Figures
plot_bar_nation_wise_participation = dv.nation_wise_participation(
    df,
    default_theme
)

plot_scatter_nation_wise_over_performing_players = dv.nation_over_performing_players(
    df,
    default_theme
)

plot_scatter_club_wise_players = dv.club_wise_player(
    df,
    default_theme
)

plot_scatter_club_wise_over_performing_players = dv.club_wise_over_performing_players(
    df,
    default_theme
)

plot_scatter_height_vs_weight_variation = dv.height_vs_weight_variation(
    df,
    default_theme
)

plot_bar_player_position = dv.players_position(
    df,
    default_theme
)

plot_histogram_age_distribution = dv.age_distribution(
    df,
    default_theme
)

# Application layout
app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row(
                dbc.Col(
                    html.Div(
                        "Team-A: Visualizing the FIFA Dataset",
                        className="display-3 text-primary text-center",
                    ),
                    class_name="center-flex mt-3",
                )
            ),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    html.Strong(
                        "FIFA: International Federation of Association Football",
                        className="display-6 mb-3 text-danger text-center",
                    ),
                    class_name="center-flex",
                )
            ),
            html.Br(),
            html.Br(),
            # 2-Text Header Rows
            dbc.Row([
                dbc.Col([
                    init_text_field(
                        "Nation-wise Participation",
                        "#barPlot_nationWiseParticipation"
                    )
                ], width=6),
                dbc.Col([
                    init_text_field(
                        "Nation-wise Over-performing Players",
                        "#scatterPlot_nationWiseOverPerformers"
                    )
                ], width=6)
            ], align='center'),
            html.Br(),
            # 2-Plot Rows
            dbc.Row([
                dbc.Col([
                    init_figure(
                        "nation_wise_participation",
                        plot_bar_nation_wise_participation
                    )
                ],
                    id="barPlot_nationWiseParticipation",
                    width=6
                ),
                dbc.Col([
                    init_figure(
                        "over_performing_players",
                        plot_scatter_nation_wise_over_performing_players
                    )
                ],
                    id="scatterPlot_nationWiseOverPerformers",
                    width=6
                ),
            ], align='center'),
            html.Br(),
            html.Br(),

            # 2-Text Header Rows
            dbc.Row([
                dbc.Col([
                    init_text_field(
                        "Club-wise Participation",
                        "#scatterPlot_clubWisePlayers"
                    )
                ], width=6),
                dbc.Col([
                    init_text_field(
                        "Club-wise Over-performing Players",
                        "#scatterPlot_clubWiseOverPerformers"
                    )
                ], width=6)
            ], align='center'),
            html.Br(),
            # 2-Plot Rows
            dbc.Row([
                dbc.Col([
                    init_figure(
                        "club_wise_players",
                        plot_scatter_club_wise_players
                    )
                ],
                    id="scatterPlot_clubWisePlayers",
                    width=6
                ),
                dbc.Col([
                    init_figure(
                        "club_wise_over_performing_players",
                        plot_scatter_club_wise_over_performing_players
                    )
                ],
                    id="scatterPlot_clubWiseOverPerformers",
                    width=6
                ),
            ], align='center'),
            html.Br(),
            html.Br(),

            # 1-Text Header Row
            dbc.Row([
                dbc.Col([
                    init_text_field(
                        "Height vs Weight Variation",
                        "#scatterPlot_heightVsWeightVariation"
                    )
                ], width=12, align='center')
            ], align='center'),
            html.Br(),
            # 1-Plot Row
            dbc.Row([
                dbc.Col([
                    init_figure(
                        "height_weight_variation",
                        plot_scatter_height_vs_weight_variation
                    )
                ],
                    id="scatterPlot_heightVsWeightVariation",
                    width=12,
                    align='center'
                ),
            ], align='center'),
            html.Br(),
            html.Br(),

            # 2-Text Header Rows
            dbc.Row([
                dbc.Col([
                    init_text_field(
                        "Player Position",
                        "#barPlot_playerPosition"
                    )
                ], width=6),
                dbc.Col([
                    init_text_field(
                        "Player Age Distribution",
                        "#histogramPlot_playerAgeDistribution"
                    )
                ], width=6)
            ], align='center'),
            html.Br(),
            # 2-Plot Rows
            dbc.Row([
                dbc.Col([
                    init_figure(
                        "player_position",
                        plot_bar_player_position
                    )
                ],
                    id="barPlot_playerPosition",
                    width=6
                ),
                dbc.Col([
                    init_figure(
                        "player_age_distribution",
                        plot_histogram_age_distribution
                    )
                ],
                    id="histogramPlot_playerAgeDistribution",
                    width=6
                ),
            ], align='center'),


        ], style={'background-color': '#fafafa'})
    )
]
#, className="dbc all-row-margin container"
)


# Method Callbacks
@app.callback(
    Output("nation_wise_participation", "figure"),
    Input(dbt.ThemeSwitchAIO.ids.switch("theme"), "value")
)
def update_figure(toggle):
    template = default_theme if toggle else dark_theme
    result_nation_wise_participation = dv.nation_wise_participation(df, template)
    return result_nation_wise_participation


@app.callback(
    Output("over_performing_players", "figure"),
    Input(dbt.ThemeSwitchAIO.ids.switch("theme"), "value")
)
def update_figure(toggle):
    template = default_theme if toggle else dark_theme
    result_over_performing_players = dv.nation_over_performing_players(df, template)
    return result_over_performing_players


@app.callback(
    Output("club_wise_players", "figure"),
    Input(dbt.ThemeSwitchAIO.ids.switch("theme"), "value")
)
def update_figure(toggle):
    template = default_theme if toggle else dark_theme
    result_club_wise_players = dv.club_wise_player(df, template)
    return result_club_wise_players


@app.callback(
    Output("club_wise_over_performing_players", "figure"),
    Input(dbt.ThemeSwitchAIO.ids.switch("theme"), "value")
)
def update_figure(toggle):
    template = default_theme if toggle else dark_theme
    result_club_wise_over_performing_players = dv.club_wise_over_performing_players(df, template)
    return result_club_wise_over_performing_players


@app.callback(
    Output("height_weight_variation", "figure"),
    Input(dbt.ThemeSwitchAIO.ids.switch("theme"), "value")
)
def update_figure(toggle):
    template = default_theme if toggle else dark_theme
    result_height_weight_variation = dv.height_vs_weight_variation(df, template)
    return result_height_weight_variation


# Run the application
if __name__ == "__main__":
    server = app.server
    app.run_server(debug=True)
