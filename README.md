# Introduction

This is a script to import datapoints into InfluxDB from a KairosDB export file.

# Requirements

- Python 3
- InfluxDB
- PyYAML

# Configuration

Edit conf/import.yml. Specify the hostname, port, login, and database used to
store the datapoints. Set export_path to the path of your export file.
