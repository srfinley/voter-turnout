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
        
            ## Process

            #### About the Data

            Voter data is available for free from the Somerset County Board of Elections. The particular dataset used here was requested in April of 2018, and exclusively covers the Green Brook, North Plainfield, and Manville municipalities. It includes all voters registered in those areas, and in addition to recording turnout for five elections from 2015-2017, the dataset features voters’ full names and street addresses.


            """
        ),

    ],
)

layout = dbc.Row([column1])