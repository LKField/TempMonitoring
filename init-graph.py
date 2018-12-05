import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import csv

with open('Test.csv') as csvfile:
    my_data = csv.reader(csvfile) # read in csv file
    next(my_data, None)
    dates = []
    temps = []
    humids = []

    for row in my_data: # read in and format rows
        date = row[0]
        temp = row[1]
        humid = row[2]

        dates.append(date)
        temps.append(temp)
        humids.append(humid)

        form_dates = pd.to_datetime(dates) # convert column 1 to datetime

#    print(form_dates)
#    print(temps)
#    print(humids)

trace1 = go.Scatter(x=form_dates, y=temps, name='Temperature (F)')
trace2 = go.Scatter(x=form_dates, y=humids, name='Relative Humidity (%)')


app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Demo Lab 1 Norwood Temperature and Humidity Data'),
    dcc.Graph(
        id='temperature-graph',
        figure={
            'data': [trace1],
            'layout':
            go.Layout(title='Temperature (F)')
        }),
    dcc.Graph(
        id='humidity-graph',
        figure={
            'data': [trace2],
            'layout':
            go.Layout(title='Relative Humidity (%)')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
