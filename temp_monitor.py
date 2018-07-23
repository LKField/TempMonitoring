from bokeh.plotting import figure, output_file, show
import bokeh.layouts
import pandas as pd
import numpy as np
import datetime

# prepare some data
my_data = pd.read_csv('Demo1.csv', parse_dates=['Timestamp for sample frequency every 15 min'])
time = my_data[my_data.columns[0]]
temp = my_data[my_data.columns[1]]
humidity = my_data[my_data.columns[2]]

print(time)

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="Temperature over Time in Demo Lab 1", x_axis_label='Time (ns)', y_axis_label='Temperature (deg F)')
p.sizing_mode='scale_height'

# add a line renderer with legend and line thickness
p.line(time, temp, legend="Temp.", line_width=2)

# show the results
show(p)
