import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predicting (un)likely voters

            This app presents a theoretically generalizable model to predict turnout among registered voters based on prior voting record and demographic information available in public voter registration records. This specific implementation of the model is based on data from Somerset County, New Jersey, and is built to predict individuals’ turnout in the 2017 general election.

            Whether you want to identify likely or unlikely voters, whether you want to advertise or offer services where they are most needed, this app fits your needs.

            """
        ),
        dcc.Link(dbc.Button('Make a New Jerseyan', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/GreenBrookZoningMap.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])