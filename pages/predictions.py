import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
            


            """
        ),
        dcc.Markdown("""##### Name"""),
        dcc.Input(
           placeholder="Your New Jerseyan",
           type='text',
           value=''
        ),
        dcc.Markdown("""##### Voting Record"""),
        dcc.Checklist(
             options=[
                     {'label': '2015 Primary', 'value': '06/02/2015'},
                     {'label': '2016 Primary', 'value': '06/07/2016'},
                     {'label': '2016 General', 'value': '11/08/2016'},
                     {'label': '2017 Primary', 'value': '06/06/2017'}
             ],
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Div(id="summary")
    ]
)


layout = dbc.Row([column1, column2])