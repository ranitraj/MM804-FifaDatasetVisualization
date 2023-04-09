import os
import pandas as pd
import figures as dv

import plotly.express as px
import dash_bootstrap_components as dbc
import dash_bootstrap_templates as dbt

from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Initialize the app & building components
app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])

# Theme Switcher
default_theme = "zephyr"
dark_theme = "vapor"
theme_switcher = dbt.ThemeSwitchAIO(
    aio_id="theme",
    themes=[dbc.themes.ZEPHYR, dbc.themes.VAPOR]
)

# Dataset
df = pd.read_csv(os.path.join("assets", "cleaned_fifa21_male2.csv"))

# Plots and Figures
plot_bar_nation_wise_participation = dv.nation_wise_participation(df, default_theme)


# Application layout
app.layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    "Team-A: Visualizing the FIFA Dataset",
                    className="display-3 text-primary text-center",
                ),
                class_name="center-flex mt-3",
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Strong(
                    "FIFA: International Federation of Association Football",
                    className="display-6 mb-3 text-danger text-center",
                ),
                class_name="center-flex",
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            dbc.Row(
                                theme_switcher, class_name="justify-content-start mb-2"
                            ),
                            html.A(
                                "Nation-wise Participation",
                                className="list-group-item list-group-item-action",
                                href="#barPlot_nationWiseParticipation",
                            )
                        ],
                        id="menu",
                        className="list-group position-fixed",
                    ),
                    width=3,
                ),
                html.Div(
                    [
                        dbc.Row(
                            dcc.Graph(
                                id="nation_wise_participation",
                                figure=plot_bar_nation_wise_participation,
                            ),
                            id="barPlot_nationWiseParticipation",
                        )
                    ],
                    className="scrollspy-example col",
                    **{"data-spy": "scroll", "data-offset": "0", "data-target": "#menu"}
                ),
            ]
        ),
    ],
    className="dbc all-row-margin container",
)


# Method Callbacks
@app.callback(
    Output("nation_wise_participation", "figure"),
    Input(dbt.ThemeSwitchAIO.ids.switch("theme"), "value")
)
def update_figure(year, toggle):
    template = default_theme if toggle else dark_theme
    fig_top_food_elements_in_year_x = dv.nation_wise_participation(df, template)
    return fig_top_food_elements_in_year_x


# Run the application
if __name__ == "__main__":
    server = app.server
    app.run_server(debug=True)
