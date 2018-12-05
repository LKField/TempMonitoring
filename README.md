# TempMonitoring
Basic program to read temperature and humidity data from Excel files and create an interactive graph to display the results 


new.py is a file based on a temperature reading data file created by Christopher Field 
An excel file with columns formatted as follows is read in and plotted
Date | Number | General 
The file must be in the working directory and is selected from a dropdown menu with all the files included. 
In the final product, this will hopefully be converted to be a drop down menu of the folders for different datasets where all the data in the folder is displayed at once and can be interacted with as a whole unit of multiple files. 

display_all2.py is the most recent program using Bokeh plots. This is not the working document, but some elements of it should be used for further iterations of the new.py code

init-graph.py is the most recent file using Dash by Plotly. Changes will include adding a dropdown menu to pick the sensor data and the function for accumulating data from multiple spreadsheet inputs.
