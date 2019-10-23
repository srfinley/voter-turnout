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

            #### Dealing with Data

            The csv file as I initially received it had two code-breaking flaws. The first, which prevented it from being read entirely, was an additional cell in one row; the second was misaligned cells in a different row, which resulted in half of that row’s entries being “off by one”. Both of these were easily fixed by manually adjusting the file in Numbers, and then I could finally load the data with Pandas for analysis. 

            It was time to get to work… except not yet. Whereas I had envisioned a file with one row per voter, and columns for voters’ turnout in each of the included elections, what I was given was a file with one row per _vote_, each dutifully labeled with the election date the vote was for and the ID number of the voter. Registered voters who voted in all five of the recorded elections were listed five times each, and those who hadn’t voted in any — almost a third of voters! — were listed once, with missing data where the election information belonged. With this haphazard kind of data structure, it would be impossible to construct a predictive model the way I’d been taught.

            I had learned the solution to this problem weeks before. After adding an additional column of nothing but the number one, I could create a pivot table with unique voter IDs as the index of the table, one per row, where each column represented one of the five elections; by using the column of ones as the “values” at the intersection of each voter and election, I laid out the pivot table such that a one would appear _only where that combination of voter ID and election had occurred in the original table_ — that is, only when that voter was recorded as having voted in that election. Missing values in the pivot table represented missed opportunities to cast votes.

            A great deal of information was lost in the conversion from the original table to a pivot table format, but using the voter ID as a key, I was able to merge the old table onto the new table so it would include the rest of the information I wanted to use for my analysis — birthdate and registration date, along with gender and political party affiliation. Once the merge was tidied, my data was ready to go.
            """
        ),

    ],
)

layout = dbc.Row([column1])