import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import csv
import glob
import os

cdir = os.getcwd()
folder_list = (next(os.walk(cdir))[1])
print(folder_list)

# create a file list of all the .csv files in the given folder
file_list = glob.glob("*.csv")
#print(file_list)

#print(os.listdir())

dates = []
temps = []
humids = []

# open all the .csv files and create separated data lists
for name in file_list:
    #print("After 'for' Opening:", name)
    with open(name) as csvfile:
        my_data = csv.reader(csvfile) # read in csv file
        next(my_data, None)

        for row in my_data: # read in and format rows
            date = row[0]
            temp = row[1]
            humid = row[2]

            dates.append(date)
            temps.append(temp)
            humids.append(humid)

            form_dates = pd.to_datetime(dates) # convert column 1 to datetime

#print(form_dates)
#print(temps)
#print(humids)

# graph the data using Dash in two separate graphs
app = dash.Dash()

# creates a dropdpown menu for later data selection, currently not in use
select = html.Div([
    dcc.Dropdown(
    id='select',
    options=[ {'label': x, 'value': x} for x in folder_list]
    )
    ],
    style={'width' : '25%',
            'display' : 'inline-block'}
)
# creates initialization of graphs, not currently in use
graph = dcc.Graph(
    id='graph',
    figure={
    'data':[]
    }
)
app.layout = html.Div(children=[select,
                                graph])

@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='select', component_property='value')]
)
def update_graph(file_list):
    # return a defined state if no file is picked
    if file_list is None:
        return None
    print("In update_graph. You've selected'{}'".format(file_list))              # For debug
    # create and sort the data frame based on input
    df = pd.DataFrame({"date": form_dates, "temp": temps, "humid": humids})
    df = df.sort_values(by=['date'])
    # create traces
    trace1 = go.Scatter(x=df.date, y=df.temp, name='Temperature (F)')
    trace2 = go.Scatter(x=df.date, y=df.humid, name='Relative Humidity (%)')
    # actually graph the data
    dcc.Graph(
        id='graph',
        figure={
            'data': [trace1, trace2],
            'layout':
            go.Layout(title='Temperature (F)')
        })

    return {'data' : [trace1, trace2]}                  # Return the two lines (traces) for plotting.

if __name__ == '__main__':
    app.run_server(debug=True)
