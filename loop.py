import pandas as pd
import matplotlib as plt
import numpy as np
from datetime import datetime, timedelta as dt
import xlrd

# define empty_cell boolean
empty_cell= False
with xlrd.open_workbook(filename='Demo1_13.xlsx') as wb:
    cs= wb.sheet_by_index(0)
    num_cols= 1     # hard code in the first column as the date
    num_rows= cs.nrows
    # set count empty and full cells
    count_full = 0
    count_empty = 0
    for row_index in range(1, num_rows):
        for col_index in range(0,num_cols):
            # get cell value
            cell_val= cs.cell(row_index, col_index).value
            # check if cell is empty
            if cell_val== '':
                # set empty cell is True
                empty_cell = True
                # increment counter
                count_empty+= 1
            else:
                # set empty cell is false (cell has value)
                empty_cell= False
                # increment counter based on the row index (assumes no empty cells within data block)
                count_full= row_index
            # check if cell is not empty
            if not empty_cell:
                # print value of cell as a datetime
                date = cs.cell_value(count_full,0)
                datetime_value = datetime(*xlrd.xldate_as_tuple(date, 0))
                print(datetime_value)
        # check the counter if is = num_cols means the whole row is empty
        if count_empty == num_cols:
            # stop looping to next rows
            break
