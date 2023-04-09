import dash_bootstrap_components as dbc
import dash_bootstrap_templates as dbt

# Initialize the app & building components
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

# Theme Switcher
default_theme = "vapor"
dark_theme = "zephyr"
theme_switcher = dbt.ThemeSwitchAIO(
    aio_id="theme",
    themes=[dbc.themes.VAPOR, dbc.themes.ZEPHYR]
)