import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from joblib import load
pipeline = load('assets/pipeline.joblib')

import pandas as pd
from datetime import datetime as dt

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
            id = 'name',
           placeholder="Your New Jerseyan",
           type='text',
           value='Michael'
        ),
        dcc.Markdown("""##### Voting Record"""),
        dcc.Checklist(
            id = 'votes',
             options=[
                     {'label': '2015 Primary', 'value': 'pri15'},
                     {'label': '2016 Primary', 'value': 'pri16'},
                     {'label': '2016 General', 'value': 'gen16'},
                     {'label': '2017 Primary', 'value': 'pri17'}
             ],
        ),
        dcc.Markdown("""##### Birthdate"""),
        dcc.DatePickerSingle(
            id='birthdate',
            number_of_months_shown=1,
            min_date_allowed=dt(1900, 1, 1),
            max_date_allowed=dt(1999, 11, 7),
            date=dt(1997, 5, 10)
        ),
        dcc.Markdown("""##### Date of Most Recent Voter Registration"""),
        dcc.DatePickerSingle(
            id='reg_date',
            number_of_months_shown=1,
            min_date_allowed=dt(1900, 1, 1),
            max_date_allowed=dt(2018, 1, 1),
            date=dt(1997, 5, 10)
        ),
        dcc.Markdown("""##### Gender"""),
        dcc.Dropdown(
            id='sex',
            options=[
                {'label': 'M', 'value': 'M'},
                {'label': 'F', 'value': 'F'},
                {'label': 'N', 'value': 'N'}
            ],
            value='N'
        ),
        dcc.Markdown("""##### Party Affiliation"""),
        dcc.Dropdown(
            id='party',
            options=[
                {'label': 'Republican', 'value': 'REP'},
                {'label': 'Democrat', 'value': 'DEM'},
                {'label': 'Other party', 'value': 'OTH'},
                {'label': 'Unaffiliated', 'value': 'UNA'}
            ],
            value='UNA'
        ),
        dcc.Markdown("""##### Municipality"""),
        dcc.Dropdown(
            id='muni',
            options=[
                {'label': 'North Plainfield', 'value': 1},
                {'label': 'Manville', 'value': 2},
                {'label': 'Green Brook', 'value': 3}
            ],
            value=1
        ),
    ],
    md=6,
)

column2 = dbc.Col(
    [
        html.Div(id="summary"),
        html.H2('Odds of voting', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ]
)

@app.callback(
    Output('prediction-content', 'children'),
    [Input('name', 'value'), Input('votes', 'value'), 
    Input('birthdate', 'date'), Input('reg_date', 'date'), 
    Input('sex', 'value'), Input('party', 'value'), Input('muni', 'value')],
)
def predict(name, votes, birthdate, reg_date, sex, party, muni):
    if votes == None:
        pri15, pri16, gen16, pri17 = 0,0,0,0
        voter_score = 0
    else:
        pri15 = 'pri15' in votes
        pri16 = 'pri16' in votes
        gen16 = 'gen16' in votes
        pri17 = 'pri17' in votes
        voter_score = len(votes)/4
    age_2017 = (pd.to_datetime('11/07/2017') - pd.to_datetime(birthdate)).days // 365
    reg_age = (pd.to_datetime(reg_date) - pd.to_datetime(birthdate)).days // 365
    since_reg = (pd.to_datetime('11/07/2017') - pd.to_datetime(reg_date)).days // 365
    male = sex == 'M'
    female = sex == 'F'
    dem = party == 'DEM'
    rep = party == 'REP'
    una = party == 'UNA'
    oth = party == 'OTH'
    if muni == None:
        muni = 1
    df = pd.DataFrame(
        columns=['11/08/2016','06/06/2017','06/07/2016','06/02/2015',
                 'male','female','age_2017','voter_score','since_reg','reg_age',
                 'dem','rep','una','3rd','municipality'], 
        data=[[gen16,pri17,pri16,pri15,
               male,female,age_2017,voter_score,since_reg,reg_age,
               dem,rep,una,oth,muni]]
    )
    y_pred = pipeline.predict(df)[0]
    y_pred_proba = pipeline.predict_proba(df)[0][1]
    return f"It's November 7th, 2017. {name} has a {(y_pred_proba*100):.2f}% chance of voting in the general election."


layout = dbc.Row([column1, column2])