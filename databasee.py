import dash
import dash_html_components as html
import dash_table
import pathlib
import sqlite3
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

DB_FILE = pathlib.Path(__file__).resolve().parent.joinpath("stock_data.db").resolve()
con = sqlite3.connect(str(DB_FILE))
statement = f'SELECT * FROM KOZAA;'
df = pd.read_sql_query(statement, con)

app = dash.Dash(__name__,
              external_stylesheets=external_stylesheets)

app.layout = html.Div([

                html.Div(
                    dash_table.DataTable(
                        id='table',
                        data=df.to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in df.columns],
                        style_cell={'textAlign': 'center'},
                        fixed_rows={'headers': True, 'data': 0},
                        style_header={'fontWeight': 'bold','backgroundColor': 'rgb(66,196,247)'}

    ))

    ],className='container')


if __name__ == '__main__':
    app.run_server(debug=True)