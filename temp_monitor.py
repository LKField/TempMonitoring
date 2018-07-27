# Temperature/Humidity analysis program to read in data from a spreadsheet
# Plot the data in a static HTML output file
# Author: Lucretia Field
# Date: July 26, 2018

from bokeh.plotting import figure, output_file, show
import bokeh.layouts
import pandas as pd
import matplotlib as plt
import numpy as np
from datetime import datetime, timedelta as dt
import xlrd

# Ask user for input names of file (later create a script or other mechanism to automate this)
my_input = ''
my_data = pd.DataFrame() # create empty data frame to populate with read in values
while my_input != 'exit':
    my_input = input("Write filename to read or type 'exit' to end: ")
    if my_input != 'exit':
        my_file = pd.read_excel(my_input, parse_dates=['Timestamp for sample frequency every 15 min']) # read in data
        my_file.set_index(keys='Timestamp for sample frequency every 15 min', drop=True, inplace=True) # set time as index
        my_data = my_data.append(my_file) # append the data to dataframe 'my_data'
        my_data = my_data.drop_duplicates(keep='first') # delete duplicates if any are present
        my_data = my_data.sort_values(['Timestamp for sample frequency every 15 min'], ascending=True) # sort the data
    else:
        break

print(my_data)
temp = my_data[my_data.columns[0]]
humidity = my_data[my_data.columns[1]]

# output to static HTML file
output_file("output.html")

# create a new plot with a title and axis labels
p = figure(title="Temperature over Time in Demo Lab 1", x_axis_type='datetime', x_axis_label='Date and Time', y_axis_label='Temperature (deg F)')
p.xaxis[0].ticker.desired_num_ticks = 30
p.yaxis[0].ticker.desired_num_ticks = 30
p.sizing_mode='scale_height'

# add a line renderer with legend and line thickness
p.line(x=my_data.index, y=temp, legend="Temp.", line_width=2)

# show the results
show(p)
