import csv
import glob
import time
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

cdir = os.getcwd()
folder_list = (next(os.walk(cdir))[1])
print(folder_list)

#find the .csv files
file_list = glob.glob('*.csv')
print(file_list)

def get_data(file_list):
    t_s = time.time()
    dfs = []
    for name in file_list:
        df = pd.read_csv(name, names=['daytime', 'temp', 'humd'],
                         skiprows=1, converters={'daytime' : pd.to_datetime})
        df.daytime = pd.to_datetime(df.daytime)
        dfs.append(df)
    df = pd.concat(dfs)
    df = df.sort_values(by=['daytime'])
    print("Time to run 'get_data is {:}".format(time.time()-t_s))
    return df, df.daytime, df.temp, df.humd

df, form_dates, temps, humids = get_data(file_list)
# print(form_dates)
# print(temps)
# print(humids)
# print(df)

trace1 = go.Scatter(x=form_dates, y=temps, name='Temperature (F)')
trace2 = go.Scatter(x=form_dates, y=humids, name='Humidity (%)')

app = dash.Dash()

select = html.Div([
    dcc.Dropdown(
        id='select',
        options=[ {'label': x, 'value': x} for x in file_list]
    )],      style={'width' : '25%',
            'display' : 'inline-block'}
)

graph = html.Div([
    dcc.Graph(
        id='graph',
        figure={
            'data': []
        })
])

app.layout = html.Div(children=[select, graph])

@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='select', component_property='value')
    ]
)
def update_graph(file_list):
    # return a defined state if no file is picked
    if file_list is None:
        return None
    print("In update_graph. You've selected'{}'".format(file_list))              # For debug

    # actually graph the data
    dcc.Graph(
        id='graph',
        figure={
            'data': [trace1, trace2]
        })

    return {
        'data' : [trace1, trace2]
    }                  # Return the two lines (traces) for plotting.

if __name__ == '__main__':
    app.run_server(debug=True)
