# -*- coding: utf8 -*-

import convert

class Configs:
    def __init__(self):
        self.basic = "http://redmine.scienbizip.com/"
        self.token = "50c5e31144b945434eb3a6dbf4470a7e7234b72b"

    def url(self, journal=True, Project="", Status="", Tracker="", Author="", Filed_Ver="", Priority="", ID="", Start="", Assigned=""):

        Name2Str = convert.Name2num()

        if journal:
            if ID == "":
                print "ID is Null. Journal case should have ID argument"
            else:
                link = self.basic + "issues/" + ID + ".json?include=journals" + "&key=" + self.token
                return link
        else:
            link = self.basic + "issues.json?" + "&key=" + self.token
            if Project:
                link = link + "&project_id=" + Name2Str.project(Project)

            if Status:
                link = link + "&status_id=" + Name2Str.status(Status)

            if Tracker:
                link = link + "&tracker_id=" + Name2Str.tracker(Tracker)

            if Author:
                link = link + "&author_id=" + Name2Str.user(Author)

            if Filed_Ver:
                link = link + "&fixed_version_id=" + Name2Str.fixedver(Filed_Ver)

            if Priority:
                link = link + "&priority_id=" + Name2Str.priority(Priority)

            if Assigned:
                link = link + "&assigned_to_id=" + Name2Str.user(Assigned)

            if Start:
                link = link + "&created_on=>=" + str(Start)

            return link

