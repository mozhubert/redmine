# -*- coding: utf8 -*-

import config
import issues

class Info:
    def priority(self, item):
        # Execute the action to get the latest information
        URL = config.Configs()
        issue = issues.Info()

        # Get the URL by priority
        PriorityURL = URL.url(False, Project='Shield', Priority=item, Filed_Ver='2.9')
        print "Priority: {}. Total amount: {}".format(item, issue.amount(PriorityURL))
        issue.list(PriorityURL)

    def assigned(self, item):
        # Execute the action to get the latest information
        URL = config.Configs()
        issue = issues.Info()

        # Get the URL by assigned user
        UserURL = URL.url(False, Project='Shield', Filed_Ver='2.9', Assigned=item)
        print "User: {} Total amount: {}".format(item, issue.amount(UserURL))
        issue.list(UserURL)

    def status(self, item):
        # Execute the action to get the latest information
        URL = config.Configs()
        issue = issues.Info()

        # Get the URL by assigned user
        StatusURL = URL.url(False, Project='Shield', Filed_Ver='2.9', Status=item)
        print "Status: {} Total amount: {}".format(item, issue.amount(StatusURL))
        issue.list(StatusURL)