from bokeh.plotting import figure, output_file, show
import bokeh.layouts
import pandas as pd
import matplotlib as plt
import numpy as np
import datetime

#Ask user for input names of file (later create a script or other mechanism to automate this)
my_input = ''
my_data = []
while my_input != 'exit':
    my_input = input("Write filename to read or type 'exit' to end: ")
    if my_input != 'exit':
        my_file = pd.read_excel(my_input, parse_dates=['Timestamp for sample frequency every 15 min'])
        print(my_file)
        my_data = my_file.append(my_file)
        continue
    if my_input == 'exit':
        my_data.sort_values(by='Timestamp for sample frequency every 15 min')
        print(my_data)
        break

time = my_data[my_data.columns[0]]
temp = my_data[my_data.columns[1]]
humidity = my_data[my_data.columns[2]]

# output to static HTML file
output_file("output.html")

# create a new plot with a title and axis labels
p = figure(title="Temperature over Time in Demo Lab 1", x_axis_label='Time (ns)', y_axis_label='Temperature (deg F)')
p.sizing_mode='scale_height'

# add a line renderer with legend and line thickness
p.line(humidity, temp, legend="Temp.", line_width=2)

# show the results
show(p)
