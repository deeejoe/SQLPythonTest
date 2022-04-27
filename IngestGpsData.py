import json
from logging import exception
from sqlite3 import Cursor
import sys
import pyodbc

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
    Cursor = con.cursor()

data = {"GpsData":[
            {"Latitude":5.313833000000000e+001,"Longitude":-1.327364000000000e+000,"LocationTime":"2021-01-28T09:07:00","ShipmentNumber":"SEZHUK-210127-000836"},
            {"Latitude":5.309736200000000e+001,"Longitude":-1.314799000000000e+000,"LocationTime":"2021-01-28T09:07:00","ShipmentNumber":"SEZHUK-210127-000836"},
            {"Latitude":5.308156600000000e+001,"Longitude":-1.296553000000000e+000,"LocationTime":"2021-01-28T09:12:00","ShipmentNumber":"SEZHUK-210127-000836"},
            {"Latitude":5.306520300000000e+001,"Longitude":-1.270203000000000e+000,"LocationTime":"2021-01-28T09:12:00","ShipmentNumber":"SEZHUK-210127-000836"},
            {"Latitude":5.304051600000000e+001,"Longitude":-1.253806000000000e+000,"LocationTime":"2021-01-28T09:17:00","ShipmentNumber":"SEZHUK-210127-000836"},
            {"Latitude":5.301510200000000e+001,"Longitude":-1.243105000000000e+000,"LocationTime":"2021-01-28T09:17:00","ShipmentNumber":"SEZHUK-210127-000836"},
            {"Latitude":5.299050000000000e+001,"Longitude":-1.233735000000000e+000,"LocationTime":"2021-01-28T09:27:00","ShipmentNumber":"SEZHUK-210127-000836"},
            {"Latitude":5.294509600000000e+001,"Longitude":-1.279453000000000e+000,"LocationTime":"2021-01-28T09:32:00","ShipmentNumber":"SEZHUK-210127-000836"},
            {"Latitude":5.292212000000000e+001,"Longitude":-1.299804000000000e+000,"LocationTime":"2021-01-28T09:37:00","ShipmentNumber":"SEZHUK-210127-000836"},
            {"Latitude":5.287117300000000e+001,"Longitude":-1.307405000000000e+000,"LocationTime":"2021-01-28T09:42:00","ShipmentNumber":"SEZHUK-210127-000836"}]
        }

json_string = json.dumps(data)

print(json_string)

try:
    Cursor = con.cursor()
    Cursor.execute('exec dbo.uspLoadGpsData @json = ?',json_string)
except exception as e:
    Cursor.rollback()
    print(e.value)
    print('Transaction rolled back')

else:
    print('Record inserted sucessfully')
    Cursor.commit()
    Cursor.close()
finally:
    con.close()
    print('Connection closeed')
        


