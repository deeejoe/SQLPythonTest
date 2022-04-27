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

data = {"ShipmentsBooking":[{"ShipmentNumber":"SEZHUK-210105-000223","CollectionPostcode":"DG16 5HT","DeliveryPostcode":"EH54 5DE","BookingDate":"2021-01-05T00:00:00","ScheduledCollectionDate":"2021-01-06T00:00:00","ScheduledDeliveryDate":"2021-01-07T00:00:00","FirstCollectionScheduleEarliest":"2021-01-06T14:00:00","FirstCollectionScheduleLatest":"2021-01-06T16:00:00","LastDeliveryScheduleEarliest":"2021-01-07T06:30:00","LastDeliveryScheduleLatest":"2021-01-07T07:00:00","VehicleType":"Tractor Unit \/ Curtain side"},
                            {"ShipmentNumber":"SEZHUK-201218-000183","CollectionPostcode":"DG16 5HT","DeliveryPostcode":"EH21 8JU","BookingDate":"2020-12-18T00:00:00","ScheduledCollectionDate":"2020-12-22T00:00:00","ScheduledDeliveryDate":"2020-12-23T00:00:00","FirstCollectionScheduleEarliest":"2020-12-22T10:00:00","FirstCollectionScheduleLatest":"2020-12-22T12:00:00","LastDeliveryScheduleEarliest":"2020-12-23T08:00:00","LastDeliveryScheduleLatest":"2020-12-23T12:00:00","VehicleType":"Tractor Unit \/ Curtain side"},
                            {"ShipmentNumber":"SEZHUK-210118-000464","CollectionPostcode":"DG16 5HU","DeliveryPostcode":"LA4 4DD","BookingDate":"2021-01-18T00:00:00","ScheduledCollectionDate":"2021-01-20T00:00:00","ScheduledDeliveryDate":"2021-01-20T00:00:00","FirstCollectionScheduleEarliest":"2021-01-20T07:00:00","FirstCollectionScheduleLatest":"2021-01-20T09:00:00","LastDeliveryScheduleEarliest":"2021-01-20T08:00:00","LastDeliveryScheduleLatest":"2021-01-20T16:00:00","VehicleType":"Tractor Unit \/ Curtain side"},
                            {"ShipmentNumber":"SEZHUK-210118-000471","CollectionPostcode":"DG16 5HU","DeliveryPostcode":"LL54 5RL","BookingDate":"2021-01-18T00:00:00","ScheduledCollectionDate":"2021-01-19T00:00:00","ScheduledDeliveryDate":"2021-01-20T00:00:00","FirstCollectionScheduleEarliest":"2021-01-19T13:00:00","FirstCollectionScheduleLatest":"2021-01-19T15:00:00","LastDeliveryScheduleEarliest":"2021-01-20T08:00:00","LastDeliveryScheduleLatest":"2021-01-20T16:00:00","VehicleType":"Tractor Unit \/ Curtain side"},
                            {"ShipmentNumber":"SEZHUK-210120-000569","CollectionPostcode":"DN8 5TG","DeliveryPostcode":"CT15 7HX","BookingDate":"2021-01-20T00:00:00","ScheduledCollectionDate":"2021-01-22T00:00:00","ScheduledDeliveryDate":"2021-01-22T00:00:00","FirstCollectionScheduleEarliest":"2021-01-21T06:00:00","FirstCollectionScheduleLatest":"2021-01-22T10:00:00","LastDeliveryScheduleEarliest":"2021-01-22T08:00:00","LastDeliveryScheduleLatest":"2021-01-22T16:00:00","VehicleType":"Tractor Unit \/ Curtain side"},
                            {"ShipmentNumber":"SEZHUK-210121-000642","CollectionPostcode":"DN8 5TG","DeliveryPostcode":"PA31 8LZ","BookingDate":"2021-01-21T00:00:00","ScheduledCollectionDate":"2021-01-22T00:00:00","ScheduledDeliveryDate":"2021-01-25T00:00:00","FirstCollectionScheduleEarliest":"2021-01-22T10:00:00","FirstCollectionScheduleLatest":"2021-01-22T12:00:00","LastDeliveryScheduleEarliest":"2021-01-25T08:00:00","LastDeliveryScheduleLatest":"2021-01-25T16:00:00","VehicleType":"Tractor Unit \/ Curtain side"},
                            {"ShipmentNumber":"SEZHUK-210122-000671","CollectionPostcode":"DN8 5TG","DeliveryPostcode":"GL4 0UG","BookingDate":"2021-01-22T00:00:00","ScheduledCollectionDate":"2021-01-25T00:00:00","ScheduledDeliveryDate":"2021-01-26T00:00:00","FirstCollectionScheduleEarliest":"2021-01-25T06:00:00","FirstCollectionScheduleLatest":"2021-01-25T21:00:00","LastDeliveryScheduleEarliest":"2021-01-26T08:30:00","LastDeliveryScheduleLatest":"2021-01-26T09:00:00","VehicleType":"Tractor Unit \/ Curtain side"},
                            {"ShipmentNumber":"SEZHUK-210127-000836","CollectionPostcode":"DN8 5TG","DeliveryPostcode":"B29 6SJ","BookingDate":"2021-01-27T00:00:00","ScheduledCollectionDate":"2021-01-28T00:00:00","ScheduledDeliveryDate":"2021-01-29T00:00:00","FirstCollectionScheduleEarliest":"2021-01-28T10:00:00","FirstCollectionScheduleLatest":"2021-01-28T12:00:00","LastDeliveryScheduleEarliest":"2021-01-29T08:00:00","LastDeliveryScheduleLatest":"2021-01-29T16:00:00","VehicleType":"Tractor Unit \/ Curtain side"},
                            {"ShipmentNumber":"SEZHUK-210202-001013","CollectionPostcode":"DN8 5TG","DeliveryPostcode":"SN8 2RN","BookingDate":"2021-02-02T00:00:00","ScheduledCollectionDate":"2021-02-03T00:00:00","ScheduledDeliveryDate":"2021-02-04T00:00:00","FirstCollectionScheduleEarliest":"2021-02-03T13:00:00","FirstCollectionScheduleLatest":"2021-02-03T15:00:00","LastDeliveryScheduleEarliest":"2021-02-04T08:00:00","LastDeliveryScheduleLatest":"2021-02-04T15:59:00","VehicleType":"Tractor Unit \/ Curtain side"},
                            {"ShipmentNumber":"SEZHUK-210202-001015","CollectionPostcode":"DN8 5TG","DeliveryPostcode":"BH16 6AG","BookingDate":"2021-02-02T00:00:00","ScheduledCollectionDate":"2021-02-03T00:00:00","ScheduledDeliveryDate":"2021-02-04T00:00:00","FirstCollectionScheduleEarliest":"2021-02-03T15:00:00","FirstCollectionScheduleLatest":"2021-02-03T17:00:00","LastDeliveryScheduleEarliest":"2021-02-04T10:00:00","LastDeliveryScheduleLatest":"2021-02-04T12:00:00","VehicleType":"Tractor Unit \/ Curtain side"}
                            ]
        }

json_string = json.dumps(data)

print(json_string)

try:
    Cursor = con.cursor()
    Cursor.execute('exec dbo.uspLoadShipmentsBooking @json = ?',json_string)
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
        


