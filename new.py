# -*- coding: utf-8 -*-

import os
import shlex, subprocess                    # Used to open Safari

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# This gets the list of file names in the current folder.
# A different path can be specified and I am sure there is a way
# to make this user pickable.
file_names = os.listdir('.')
# This print just confirms that we got a list.
print(file_names)
# It is possible to filter this list so that only excel files are included.

app = dash.Dash()

# This defines a dropdown menu populated with all of the files in the folder
select = html.Div([
    dcc.Dropdown(
        id='select',
        options=[ {'label' : x, 'value' : x } for x in file_names],
        )
    ],
    style={'width' : '25%',
           'display' : 'inline-block'}
    )

# box = dcc.Input(id='pick', value='initial value', type='text')
#
# This defines a graph that currently has nothing in it.
graph = dcc.Graph(id='graph')

# This tells dash about the two objects.
app.layout = html.Div(children=[select,
                                graph] )
# The "@" defines a 'decrorator' which does something to the following
# function. In this case, the decorator defines a source (the drop down menu)
# and defines a destination (the graph).
# The following function (update_graph) converts the input (a file name)
# into an output (the specifications for a plot). There can be more than one
# souce, which is why it is in a list.
@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='select', component_property='value')]
)
def update_graph(file_name):
    if file_name is None:                               # Return a defined state if no file is picked
        return None
    print("In update_graph. You've selected'{}'".format(file_name))              # For debug
    # Read the excel file. We skip the first line becasue it is not part of the tabular data.
    df = pd.read_excel(file_name, header=1)
    trace1 = go.Scatter(x=df['Date'],                   # Extract the data for the first line
                        y=df['Temp'],
                        mode='lines+markers',
                        name="Temperature"
                       )
    trace2 = go.Scatter(x=df['Date'],                   # and the data for the second line
                        y=df['Temp2'],
                        mode='lines+markers',
                        name="Humidity"
                       )
    return {'data' : [trace1, trace2]}                  # Return the two lines (traces) for plotting.


if __name__ == '__main__':
    print("Running main.")

    # Open a Safari window to open -a Safari http://127.0.0.1:8050
    # subprocess.check_call(shlex.split("open -a Safari http://127.0.0.1:8050"))

    app.run_server(debug=True)


"""
I found this source helpful
http://pbpython.com/plotly-dash-intro.html

Other references:
https://dash.plot.ly/getting-started-part-2
https://medium.com/@plotlygraphs/introducing-plotly-py-3-0-0-7bb1333f69c6
https://plot.ly/python/line-and-scatter/
https://plot.ly/python/reference/

dash conda installations instructions at
https://stackoverflow.com/questions/49613878/python-install-dash-with-conda
conda install -c conda-forge dash-renderer
conda install -c conda-forge dash
conda install -c conda-forge dash-html-components
conda install -c conda-forge dash-core-components
conda install -c conda-forge plotly

or in a single line
conda install -c conda-forge dash-renderer dash dash-html-components dash-core-components plotly

"""
