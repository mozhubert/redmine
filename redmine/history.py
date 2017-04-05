# -*- coding: utf8 -*-

import config
import issues
import requests
import json
import journals
import datetime
import influx


class History:
    def __init__(self):
        self.preInflux = {"Created_date": "", "measurement": "Shield", "tag": "Issues", "New": 0, "Assigned": 0,
                          "In_progress": 0, "Postpone": 0, "Resume": 0, "Known_issue": 0, "Feedback": 0, "Failed": 0,
                          "Resolved": 0, "Need_info": 0, "Rejected": 0, "Closed": 0, "Cancel": 0, "Non_closed": 0,
                          "Resolved_Closed": 0, "Total": 0}

        self.nowInflux = {"Created_date": "", "measurement": "Shield", "tag": "Issues", "New": 0, "Assigned": 0,
                          "In_progress": 0, "Postpone": 0, "Resume": 0, "Known_issue": 0, "Feedback": 0, "Failed": 0,
                          "Resolved": 0, "Need_info": 0, "Rejected": 0, "Closed": 0, "Cancel": 0, "Non_closed": 0,
                          "Resolved_Closed": 0, "Total": 0}

    def query(self, start, end):
        URL = config.Configs()

        queryURL = URL.url(journal=False, Project='Shield', Filed_Ver='2.9', Status='All') + "&created_on=><" + str(start) + "|" + str(end)
        # print queryURL

        bug = issues.Info()
        comment = journals.Journal()
        insertdata = influx.Influx()

        # Get the id list of queryURL
        buglist = bug.idlist(queryURL)
        print len(buglist)
        print buglist

        # Get the journal history of each ticket
        for id in buglist:
            comment.history(str(id))

        print comment.bugnum
        date_start = datetime.datetime.strptime(start, '%Y-%m-%d')
        date_end = datetime.datetime.strptime(end, '%Y-%m-%d')
        date_diff = (date_end - date_start).days

        for day in range(date_diff+1):
            print "------ Before operation data -----"
            print self.preInflux
            print self.nowInflux
            date_last = (date_start + datetime.timedelta(days=(day-1))).strftime('%Y-%m-%d')
            date_now = (date_start + datetime.timedelta(days=day)).strftime('%Y-%m-%d')
            self.preInflux["Created_date"] = date_last
            self.nowInflux["Created_date"] = date_now

            dayURL = URL.url(journal=False, Project='Shield', Filed_Ver='2.9', Status='All') + "&created_on=" + date_now

            # Get the amount of bugs by day

            if date_now in comment.bugnum.keys():
                self.nowInflux["New"] = self.preInflux["New"] + comment.bugnum[date_now]["To"]["New"] - comment.bugnum[date_now]["From"]["New"] + bug.amount(dayURL)
                self.nowInflux["Assigned"] = self.preInflux["Assigned"] + comment.bugnum[date_now]["To"]["Assigned"] - comment.bugnum[date_now]["From"]["Assigned"]
                self.nowInflux["In_progress"] = self.preInflux["In_progress"] + comment.bugnum[date_now]["To"]["In Progress"] - comment.bugnum[date_now]["From"]["In Progress"]
                self.nowInflux["Postpone"] = self.preInflux["Postpone"] + comment.bugnum[date_now]["To"]["Postpone"] - comment.bugnum[date_now]["From"]["Postpone"]
                self.nowInflux["Resume"] = self.preInflux["Resume"] + comment.bugnum[date_now]["To"]["Resume"] - comment.bugnum[date_now]["From"]["Resume"]
                self.nowInflux["Known_issue"] = self.preInflux["Known_issue"] + comment.bugnum[date_now]["To"]["Known Issue"] - comment.bugnum[date_now]["From"]["Known Issue"]
                self.nowInflux["Feedback"] = self.preInflux["Feedback"] + comment.bugnum[date_now]["To"]["Feedback"] - comment.bugnum[date_now]["From"]["Feedback"]
                self.nowInflux["Failed"] = self.preInflux["Failed"] + comment.bugnum[date_now]["To"]["Failed"] - comment.bugnum[date_now]["From"]["Failed"]
                self.nowInflux["Resolved"] = self.preInflux["Resolved"] + comment.bugnum[date_now]["To"]["Resolved"] - comment.bugnum[date_now]["From"]["Resolved"]
                # self.nowInflux["Resolved"] = self.preInflux["Resolved"] + comment.bugnum[date_now]["To"]["Resolved"]
                self.nowInflux["Need_info"] = self.preInflux["Need_info"] + comment.bugnum[date_now]["To"]["Request More Info"] - comment.bugnum[date_now]["From"]["Request More Info"]
                self.nowInflux["Rejected"] = self.preInflux["Rejected"] + comment.bugnum[date_now]["To"]["Rejected"] - comment.bugnum[date_now]["From"]["Rejected"]
                self.nowInflux["Closed"] = self.preInflux["Closed"] + comment.bugnum[date_now]["To"]["Closed"] - comment.bugnum[date_now]["From"]["Closed"]
                self.nowInflux["Cancel"] = self.preInflux["Cancel"] + comment.bugnum[date_now]["To"]["Cancel"] - comment.bugnum[date_now]["From"]["Cancel"]
                self.nowInflux["Resolved_Closed"] = self.preInflux["Resolved_Closed"] + comment.bugnum[date_now]["To"]["Resolved"] - comment.bugnum[date_now]["From"]["Resolved"] + comment.bugnum[date_now]["To"]["Closed"]
                # self.nowInflux["Non_closed"] = self.preInflux["Non_closed"] + comment.bugnum[date_now]["To"]["Non_closed"] - comment.bugnum[date_now]["From"]["Non_closed"]
            else:
                self.nowInflux["New"] = self.preInflux["New"] + bug.amount(dayURL)
                self.nowInflux["Assigned"] = self.preInflux["Assigned"]
                self.nowInflux["In_progress"] = self.preInflux["In_progress"]
                self.nowInflux["Postpone"] = self.preInflux["Postpone"]
                self.nowInflux["Resume"] = self.preInflux["Resume"]
                self.nowInflux["Known_issue"] = self.preInflux["Known_issue"]
                self.nowInflux["Feedback"] = self.preInflux["Feedback"]
                self.nowInflux["Failed"] = self.preInflux["Failed"]
                self.nowInflux["Resolved"] = self.preInflux["Resolved"]
                self.nowInflux["Resolved_Closed"] = self.preInflux["Resolved_Closed"]
                self.nowInflux["Need_info"] = self.preInflux["Need_info"]
                self.nowInflux["Rejected"] = self.preInflux["Rejected"]
                self.nowInflux["Closed"] = self.preInflux["Closed"]
                self.nowInflux["Cancel"] = self.preInflux["Cancel"]
                # self.nowInflux["Non_closed"] = self.preInflux["Non_closed"]

            self.nowInflux["Total"] = self.preInflux["Total"] + bug.amount(dayURL)
            self.preInflux["Total"] = self.nowInflux["Total"]
            self.nowInflux["Non_closed"] = self.nowInflux['Total'] - self.nowInflux['Closed']

            # The above steps has finished the operations, so the current data has been changed to last day data.
            self.preInflux["New"] = self.nowInflux["New"]
            self.preInflux["Assigned"] = self.nowInflux["Assigned"]
            self.preInflux["In_progress"] = self.nowInflux["In_progress"]
            self.preInflux["Postpone"] = self.nowInflux["Postpone"]
            self.preInflux["Resume"] = self.nowInflux["Resume"]
            self.preInflux["Known_issue"] = self.nowInflux["Known_issue"]
            self.preInflux["Feedback"] = self.nowInflux["Feedback"]
            self.preInflux["Failed"] = self.nowInflux["Failed"]
            self.preInflux["Resolved"] = self.nowInflux["Resolved"]
            self.preInflux["Resolved_Closed"] = self.nowInflux["Resolved_Closed"]
            self.preInflux["Need_info"] = self.nowInflux["Need_info"]
            self.preInflux["Rejected"] = self.nowInflux["Rejected"]
            self.preInflux["Closed"] = self.nowInflux["Closed"]
            self.preInflux["Cancel"] = self.nowInflux["Cancel"]
            # self.preInflux["Non_closed"] = self.nowInflux["Non_closed"]


            print "------ After operation data -----"
            print self.preInflux
            print self.nowInflux

            insertdata.write(self.nowInflux)