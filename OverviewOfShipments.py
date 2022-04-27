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
    df = pd.read_sql('select CAST(scheduledCollectionDate as date) as CollectionDate, VehicleType, CollectionPostcode, count(1) as NoOfShipments from ShipmentsBooking group by VehicleType, CAST(scheduledCollectionDate as date), CollectionPostcode',con=con)
    print(df)

    df1 = pd.read_sql('select CAST(scheduledCollectionDate as date) as CollectionDate, VehicleType, DeliveryPostcode, count(1) as NoOfShipments from ShipmentsBooking group by VehicleType, CAST(scheduledCollectionDate as date), DeliveryPostcode',con=con)
    print(df1)

    df2 = pd.read_sql('select CAST(scheduledCollectionDate as date) as CollectionDate, VehicleType, count(1) as NoOfShipments from ShipmentsBooking group by VehicleType, CAST(scheduledCollectionDate as date)',con=con)
    print(df2)

        


