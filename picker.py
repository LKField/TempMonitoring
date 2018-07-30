# myapp.py

from random import random
from datetime import datetime, timedelta as dt
from pathlib import Path
import pandas as pd

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
from bokeh.models.widgets import RadioGroup

# create a plot and style its properties
p = figure(x_range=(0, 100), y_range=(0, 100), toolbar_location=None)
p.border_fill_color = 'black'
p.background_fill_color = 'black'
p.outline_line_color = None
p.grid.grid_line_color = None

# add a text renderer to our plot (no data yet)
r = p.text(x=[], y=[], text=[], text_color=[], text_font_size="20pt",
           text_baseline="middle", text_align="center")

i = 0

name = ["Demo1", "Demo2", "Eng1", "Eng2"]
ds = r.data_source

# create a callback that will add a number in a random location
def callback():
    global i, my_input
    my_data = pd.DataFrame() # create empty data frame to populate with read in values
    print(name[i])
    my_input = name[i]
    print(my_input)
    i = i + 1

    pathlist = Path(my_input).glob('**/*.csv') # gather all files in folder
    # iterate through the provided folder and load all files to my_data
    for path in pathlist:
        path_in_str = str(path)
        my_file = pd.read_csv(path, parse_dates=['Timestamp for sample frequency every 15 min']) # read in data from chosen folder
        my_file.set_index(keys='Timestamp for sample frequency every 15 min', drop=True, inplace=True) # set time as index
        my_data = my_data.append(my_file) # append the data to dataframe 'my_data'
        my_data = my_data.sort_values(['Timestamp for sample frequency every 15 min'], ascending=True) # sort the data

    print(my_data)


# add a button widget and configure with the call back
button = Button(label="Press Me")
button.on_click(callback)

# radio = RadioGroup(labels=["Demo Sensor 1", "Demo Sensor 2", "Eng Sensor 1", "Eng Sensor 2"], active=0)
# radio.on_change(callback)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(button, p))
