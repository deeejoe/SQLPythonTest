# SQLPythonTest

Instructions to run.
1.	Open SQL server database and run the code from following files
dbo.GpsData – creates GpsData table
dbo.ShipmentsBooking – creates dbo.ShipmentsBooking table
uspLoadGpsData – creates stored procedure uspLoadGpsData
uspLoadShipmentsBooking – creates stored procedure uspLoadShipmentsBooking

2.	Run IngestGpsData.py file to load Gpsdata from Jason into SQL table – this could be automated to load data on-demand/real time basis
3.	Run IngestShipmentsBooking.py file to load shipments Booking data from Jason into SQL table – this could be automated to load data on-demand/real time basis
4.	Run OverviewOfShipments.py file to get the overview of shipments
5.	Run WeeklyPercentage.py to get the weekly percentage of shipments delivered on time
