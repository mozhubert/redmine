# -*- coding: utf8 -*-
from influxdb import InfluxDBClient

class Influx:
    def write(self, data):
        json_body = [
            {
                "measurement": data["measurement"],
                "tags": {
                    "project": data["tag"]
                },
                "time": data["Created_date"],
                "fields": {
                    "New": data["New"], "Assigned": data["Assigned"], "In_Progress": data["In_progress"],
                    "Postone": data["Postpone"], "Resume": data["Resume"], "Know_issue": data["Known_issue"],
                    "Feedback": data["Feedback"], "Failed": data["Failed"], "Resolved": data["Resolved"],
                    "Need_info": data["Need_info"], "Rejected": data["Rejected"], "Closed": data["Closed"],
                    "Cancel": data["Cancel"], "Total": data["Total"], "Non_closed": data["Non_closed"],
                    "Resolved_Closed": data["Resolved_Closed"]
                }
            }
        ]


        client = InfluxDBClient('10.60.229.61', 8086, 'root', 'root', 'redmine')
        client.create_database('redmine')
        client.write_points(json_body)