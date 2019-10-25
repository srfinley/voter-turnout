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
        
            ## Insights

            Most people don’t vote.

            Most _registered voters_ don’t vote.

            Out of the 21,960 registered voters in the Green Brook, North Plainfield, and Manville areas, only 7,876 — 36.3% —  voted in the election of November 7th, 2017. This value was considerably higher for the 2016 general election, but much lower for the three primary elections in the dataset.

            Who does vote? _Voters_ vote. 

            """
        ),
        html.Div([dcc.Link(dbc.Button('Become a voter', color='primary'), href='https://www.usa.gov/register-to-vote')], style={'marginBottom': '10px'}),
        dcc.Markdown(
            """

            This seemingly tautological statement is borne out by the model. More than participation in any particular past election, more than age or party affiliation, having been a frequent voter in the past raises the odds of voting in the future.


            """
        ),
        html.Img(src='assets/eli5.png', className='img-fluid'),
        dcc.Markdown(
            """
            Voter score, an engineered feature that simply refers to the voter’s rate of voting in the four elections prior to the one the model predicts, has a greater importance (represented in the above “eli5” chart as **Weight**) than every other feature combined. 

            Check out the following partial dependence plot (PDP), which elegantly demonstrates the importance of voter score (from zero to one along the x axis) to the predicted outcome of the model (y axis). 
        
            """
        ),
        html.Img(src='assets/pdp.png', className='img-fluid'),
        dcc.Markdown(
            """
            The dark line represents the average effect of voter score on the model’s predicted outcome (that they vote in November 2017 or not). There’s a substantial range in actual effect, as shown by the pale blue area surrounding the line, but the relationship is strong and clear.

            On the other hand, here’s the PDP for the second most important feature, time since registration — that is, how long it had been on election day since the voter’s most recent registration date.        
            """
        ),
        html.Img(src='assets/pdp2.png', className='img-fluid'),
        dcc.Markdown(
            """
            Although the relationship in this plot is still clear, it’s much less impressive than the first one. The pale blue mass does eventually depart from the x axis line, but seemingly only begrudgingly; it is distributed more widely around the average than the first and never reaches its heights.

            But in a sophisticated model like this, it’s not just about the individual features, but how they interact. As it turns out, the combination of voter score and time since registration has a striking relationship to the result. 
            """
        ),
        html.Img(src='assets/pdp3.png', className='img-fluid'),
        dcc.Markdown(
            """
            The numbers (and corresponding colors) at each intersection correspond to the voting rate for each cell, defined by a combination of voter score and time since registration. On the far left side, among those with voter scores of zero, time since registration makes very little difference to that solid wall of purple, but with each successive voter score increase, there is a greater range of colors across the spectrum of “since_reg” scores — meaning, the effect that time since registration has is primarily on voters with high voter scores.
            
            #### Thinking broadly

            Predicting things that already happened in one small place is easy mode. How well can we expect the model to generalize?

            Aside from municipality — a feature of marginal importance — none of the model inputs are specific to Somerset County. By excluding that, or refitting the model to accept a longer list of possible municipalities, we could easily end up with a model that would produce high-quality turnout predictions for an arbitrarily large swath of the United States.

            What about other elections? As a target, the election I chose has some specific qualities: it was a general election rather than a primary, and an off-year election (in New Jersey, most notably for the governorship and state legislature) rather than a true midterm or presidential election. Nevertheless, I believe the general principles behind the model are sound and broadly applicable. Voter score matters. For a general election, voting in the associated primary matters, as well as the preceding general. What matters most in a primary? In a presidential election? The model doesn’t directly answer these questions.
            """
        ),
    ],
    md=9,
)


column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1, column2])