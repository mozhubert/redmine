# -*- coding: utf8 -*-

import config
import json
import requests
import convert

class Journal:
    def __init__(self):
        self.bugnum = {}

    def history(self, Id):
        Str2Name = convert.Num2Name()

        URL = config.Configs()
        parseURL = URL.url(journal=True, ID=Id)
        res = requests.get(parseURL)
        doc = json.loads(res.text)
        if len(doc['issue']['journals']) > 0:
            journals = doc['issue']['journals']
            for i in range(len(journals)):
                detail = journals[i]['details']
                for j in range(len(detail)):
                    if detail[j]['name'] == 'status_id':
                        commentdate = journals[i]['created_on'][:10]
                        old_status = Str2Name.status(detail[j]['old_value'])
                        new_status = Str2Name.status(detail[j]['new_value'])
                        # print "Issue:", Id
                        # print commentdate
                        # print old_status, "->", new_status

                        if self.bugnum.has_key(commentdate):
                            self.bugnum[commentdate]['From'][old_status] = self.bugnum[commentdate]['From'][old_status] + 1
                            self.bugnum[commentdate]['To'][new_status] = self.bugnum[commentdate]['To'][new_status] + 1
                        else:
                            self.bugnum[commentdate] = {'From': {'New': 0, 'In Progress': 0, 'Resolved': 0, 'Feedback': 0,
                                                                 'Closed': 0, 'Rejected': 0, 'Request More Info': 0,
                                                                 'Postpone': 0, 'Cancel': 0, 'Resume': 0, 'Assigned': 0,
                                                                 'Failed': 0, 'Obsolete': 0, 'Known Issue': 0},
                                                        'To': {'New': 0, 'In Progress': 0, 'Resolved': 0, 'Feedback': 0,
                                                               'Closed': 0, 'Rejected': 0, 'Request More Info': 0,
                                                               'Postpone': 0, 'Cancel': 0, 'Resume': 0, 'Assigned': 0,
                                                               'Failed': 0, 'Obsolete': 0, 'Known Issue': 0}
                                                        }
                            self.bugnum[commentdate]['From'][old_status] = self.bugnum[commentdate]['From'][old_status] + 1
                            self.bugnum[commentdate]['To'][new_status] = self.bugnum[commentdate]['To'][new_status] + 1
