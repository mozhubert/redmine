# -*- coding: utf8 -*-

import config
import ongoing
import journals
import issues
import history
import influx
import datetime

PriorityList = ["P1", "P2", "P3", "P4"]
UserList = ["Wayne", "Kimi", "Willy", "Hubert", "David", "Winny", "Siang"]
StatusList = ["New", "In Progress", "Resolved", "Feedback", "Closed", "Rejected", "Request More Info", "Postpone",
              "Cancel", "Resume", "Assigned", "Failed", "Obsolete", "Known Issue"]

nonclosed = ongoing.Info()
comment = journals.Journal()
issue = history.History()
datenow = datetime.datetime.now().strftime("%Y-%m-%d")
issue.query('2017-01-01', datenow)

# DB = influx.Influx()
# DB.write('2017-03-07')

# # Show the amount and issue list according to the above status list
# for status in StatusList:
#     nonclosed.status(status)

# comment.history("28314")







