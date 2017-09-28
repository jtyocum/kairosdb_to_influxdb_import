#!/usr/bin/python3

from influxdb import InfluxDBClient
client = InfluxDBClient('toto.deohs.washington.edu', 8086, 'root', 'root', 'import6')
result = client.query('select value from Dylos48 group by *;')
print("Result: {0}".format(result))