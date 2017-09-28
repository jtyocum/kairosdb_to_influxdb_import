#!/usr/bin/python3

'''
Imports KairosDB export into InfluxDB.
'''

import os
import json
import yaml
from influxdb import InfluxDBClient

def main():

    conf_path = os.path.dirname(os.path.abspath(__file__)) + r'/conf/import.yml'
    config = yaml.load(open(conf_path, 'r'))

    client = InfluxDBClient(
        config['influxdb_host'],
        config['influxdb_port'],
        config['influxdb_user'],
        config['influxdb_pass'],
        config['influxdb_db'])
    client.create_database(config['influxdb_db'])

    kairosdb_export = open(config['export_path'], 'r')

    for row in kairosdb_export:
        row_decoded = json.loads(row)

        datapoints = []

        for datapoint in row_decoded['datapoints']:

            datapoints.append(
                {
                    "measurement": row_decoded['name'],
                    "tags": row_decoded['tags'],
                    "time": int(datapoint[0]),
                    "fields": {
                        "value": float(datapoint[1]),
                    }
                }
            )

        client.write_points(datapoints, time_precision='ms')

if __name__ == '__main__':
    main()
