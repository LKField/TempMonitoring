from bokeh.plotting import figure, output_file, show
import bokeh.layouts
import pandas as pd
import matplotlib as plt
import numpy as np
from datetime import datetime, timedelta as dt
import xlrd

# Ask user for input names of file (later create a script or other mechanism to automate this)
my_input = ''
my_data = pd.DataFrame()
while my_input != 'exit':
    my_input = input("Write filename to read or type 'exit' to end: ")
    if my_input != 'exit':
        my_file = pd.read_excel(my_input, parse_dates=['Timestamp for sample frequency every 15 min'])
        my_file.set_index(keys='Timestamp for sample frequency every 15 min', drop=True, inplace=True)
        my_data = my_data.append(my_file)
        my_data.drop_duplicates(keep=False)
    else:
        break

print(my_data)
temp = my_data[my_data.columns[0]]
humidity = my_data[my_data.columns[1]]

# output to static HTML file
output_file("output.html")

# create a new plot with a title and axis labels
p = figure(title="Temperature over Time in Demo Lab 1", x_axis_label='Time (ns)', y_axis_label='Temperature (deg F)')
p.sizing_mode='scale_height'

# add a line renderer with legend and line thickness
p.line(x=my_data.index.values, y=temp, legend="Temp.", line_width=2)

# show the results
show(p)
