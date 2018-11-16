# Temperature/Humidity analysis program to read in data from a spreadsheet
# Plot the data in a static HTML output file
# Author: Lucretia Field
# Date: July 2018

import pandas as pd
import matplotlib as plt
import numpy as np
from datetime import datetime, timedelta as dt
from pathlib import Path
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.layouts import row, widgetbox, gridplot
from bokeh.models import HoverTool
from bokeh.models.widgets import Select, RangeSlider, RadioGroup, Panel, Tabs

my_data = pd.DataFrame() # initialize empty data frame
my_folder = pd.DataFrame()

radio_group = RadioGroup(labels=["Demo Sensor 1", "Demo Sensor 2", "Eng Sensor 1", "Eng Sensor 2"], active=0)

folder_name = ['Demo1']
for name in folder_name:
    print('Current Folder: ', name)
    my_input = name
    pathlist = Path(my_input).glob('**/*.csv') # gather all files in folder
    # iterate through the provided folder and load all files to my_data
    for path in pathlist:
        path_in_str = str(path)
        my_file = pd.read_csv(path, parse_dates=['Timestamp for sample frequency every 15 min']) # read in data from chosen folder
        my_file.set_index(keys='Timestamp for sample frequency every 15 min', drop=True, inplace=True) # set time as index
        my_data = my_data.append(my_file) # append the data to dataframe 'my_data'
        my_data = my_data.sort_values(['Timestamp for sample frequency every 15 min'], ascending=True) # sort the data
    print(my_data)
    # define temperature and humidity data
    temp = my_data[my_data.columns[0]]
    humidity = my_data[my_data.columns[1]]

    # create two new plots with a title and axis labels
    p1 = figure(title="Temperature over Time", plot_width=800, x_axis_type='datetime', x_axis_label='Date and Time', y_axis_label='Temperature (deg F)')
    p1.xaxis[0].ticker.desired_num_ticks = 20 #set number of marks in graphs
    p1.yaxis[0].ticker.desired_num_ticks = 20

    p2 = figure(title="Humidity over Time", plot_width=800, x_axis_type='datetime', x_axis_label='Date and Time', y_axis_label='Humidity (%)', x_range=p1.x_range)
    p2.xaxis[0].ticker.desired_num_ticks = 20
    p2.yaxis[0].ticker.desired_num_ticks = 20

    # add a line renderer with legend and line thickness
    p1.line(x=my_data.index, y=temp, line_width=2, legend="Temperature")
    p2.line(x=my_data.index, y=humidity, line_width=2, legend="Humidity")

# select = Select(title="Choose Lab and Sensor:", value="None", options=["Demo Sensor 1", "Demo Sensor 2", "Eng Sensor 1", "Eng Sensor 2"])
# range_slider = RangeSlider(start=0, end=10, value=(1,9), step=.1, title="Date")
grid = gridplot([[p1,p2],[widgetbox(radio_group)]])

output_file("plot.html")
# show the results
show(grid)
