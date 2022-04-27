import json
from logging import exception
from sqlite3 import Cursor
import sys
import pyodbc
import pandas as pd


try:
    con = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=(local);'
    'Database=Dev;'
    'Trusted_Connection=yes;'
    'Connection Timeout=30;'
)
except exception as e:
    print(e)
    print(' Task is terminated')
    sys.exit()
else:
    df = pd.read_sql('select sum(iif(CAST(scheduleddeliveryDate as date)=  CAST(LastDeliveryScheduleLatest as date),1,0))/COUNT(1) * 100 from ShipmentsBooking',con=con)
    print('weekly percentage of shipments that are delivered on time')
    print(df,'%')

           


