import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Output, Input, State
import pandas_datareader.data as web
import datetime
from dateutil.relativedelta import relativedelta

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash(__name__,
              external_stylesheets=external_stylesheets)

app.layout = html.Div([
        html.Div([
            html.Div(html.H1('Proof-it Home')),
            #html.Img(src='/assets/icons8-p-64.png')
            ], className='banner'),
        html.Div([
            html.Div([
                dcc.Input(id='stock-input', type='text', value='AAPL'),
                html.Button('Submit', id='submit-button', n_clicks=0, style={'backgroundColor': 'rgba(255, 0, 0, 0.8)', 'color': 'white'})
            ]),
            html.Div(
                dcc.Dropdown(
                    options=[
                        {'label': 'Candlestick', 'value': 'Candlestick'},
                        {'label': 'Line', 'value': 'Line'},
                    ]
                )
            ),
            html.Div( id='stock-chart',
                    className='twelve columns'),

            html.Div( id='stock-table',
                     className='twelve columns')

    ],className='container')
        ])


@app.callback(
            [Output(component_id='stock-chart',component_property='children'),
            Output(component_id='stock-table',component_property='children')],
            [Input(component_id='submit-button',component_property='n_clicks')],
            [State(component_id='stock-input',component_property='value')]
              )

def update_fig(n_clicks, input_value):

    start = datetime.datetime.today() - relativedelta(years=5)
    end = datetime.datetime.today()
    df = web.DataReader(input_value, 'yahoo', start, end).reset_index()
    df['i'] = [i for i in range(1,len(df)+1)]
    #df['19d mean'] = ''
    #df.Date = df.Date.map(lambda x: x.strftime('%d-%m-%Y'))

    return dcc.Graph(
        id='graph',
        figure={
            'data': [
                {'x': df.Date, 'y': df.Close, 'type': 'line', 'name': input_value}
            ],
            'layout': {
                'title': input_value
            }
        }
    ), dash_table.DataTable(
        id='table',
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        style_cell={'textAlign': 'center'},
        fixed_rows={'headers': True, 'data': 0},
        style_header={'fontWeight': 'bold','backgroundColor': 'rgb(66,196,247)'}

    )



if __name__ == '__main__':
    app.run_server(debug=True)