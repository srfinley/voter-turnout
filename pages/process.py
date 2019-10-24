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

            Voter data is available for free from the Somerset County Board of Elections. The particular dataset used here was requested in April of 2018, and exclusively covers the Green Brook, North Plainfield, and Manville areas. It includes all voters registered in those areas, and in addition to recording votes for five elections from 2015-2017, the dataset features:

            * Voter ID number
            * Registration status
            * Party affiliation
            * Full name
            * Sex
            * Street and mailing address
            * Date of birth
            * Date of most recent voter registration
            * Type of ballot used in each vote
            * Various geographic distinctions: county precinct, ward, and district

            #### Dealing with Data

            The csv file as I initially received it had two code-breaking flaws. The first, which prevented it from being read entirely, was an additional cell in one row; the second was misaligned cells in a different row, which resulted in half of that row’s entries being “off by one”. Both of these were easily fixed by manually adjusting the file in Numbers, and then I could finally load the data with Pandas for analysis. 

            It was time to get to work… except not yet. Whereas I had envisioned a file with one row per voter, and columns for voters’ turnout in each of the included elections, what I was given was a file with one row per _vote_, each dutifully labeled with the election date the vote was for and the ID number of the voter. Registered voters who voted in all five of the recorded elections were listed five times each, and those who hadn’t voted in any — almost a third of voters! — were listed once, with missing data where the election information belonged. With this haphazard kind of data structure, it would be impossible to construct a predictive model the way I’d been taught.

            I had learned the solution to this problem weeks before. After adding an additional column of nothing but the number one, I could create a pivot table with unique voter IDs as the index of the table, one per row, where each column represented one of the five elections; by using the column of ones as the “values” at the intersection of each voter and election, I laid out the pivot table such that a one would appear _only where that combination of voter ID and election had occurred in the original table_ — that is, only when that voter was recorded as having voted in that election. Missing values in the pivot table represented missed opportunities to cast votes.

            A great deal of information was lost in the conversion from the original table to a pivot table format, but using the voter ID as a key, I was able to merge the old table onto the new table so it would include the rest of the information I wanted to use for my analysis — birthdate and registration date, along with gender and political party affiliation. Once the merge was tidied, my data was ready to go.

            #### Evaluating the model
            
            The model I ended up fitting was an XGBoost Classifier. To evaluate it, I used Receiver Operating Characteristic Area Under Curve (ROC AUC), and saw substantial improvements over the baseline score of .5; when I completed my analysis, I had a validation ROC AUC of .87.

            Of course, ROC AUC isn’t the only way to evaluate my model’s performance.
            """
        ),
        html.Img(src='assets/confusionmatrix.png', className='img-fluid'),
        dcc.Markdown(
            """
            In a confusion matrix like the above, all four combinations of accurate/inaccurate predictions of voting/non-voting are displayed in a grid. The left half represents instances of predicted non-voting, and the right half represents instances of predicted voting; the top half represents instances of actual non-voting, and the bottom half represents instances of actual voting. The number (along with its associated color) in each quadrant represents how many voters in the validation set fell into that combination of predicted and actual voting patterns. By looking at the relationships of these numbers, we can calculate the model’s accuracy, precision, and recall: 80%, 77%, and 63%, respectively. This represents a substantial improvement over the baseline model (just guessing the most common result, non-voting, for each voter), which in this case has an accuracy score of 64%.
            """
        )

    ],
    md=9,
)

layout = dbc.Row([column1])