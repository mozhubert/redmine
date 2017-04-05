# -*- coding: utf8 -*-

class Name2num:
    def status(self,name):
        status = {'New': '1', 'In Progress': '2', 'Resolved': '3', 'Feedback': '4', 'Closed': '5', 'Rejected': '6',
                  'Request More Info': '8', 'Postpone': '9', 'Cancel': '11', 'Resume': '12', 'Assigned': '13',
                  'Failed': '14', 'Obsolete': '15', 'Known Issue': '16'}

        if name == 'All':
            return '*'
        elif name in status:
            return status[name]
        else:
            return "Incorrect Data"

    def priority(self, name):
        priority = {'P4': '3', 'P3': '4', 'P2': '5', 'P0': '6', 'P1': '7'}

        if name == 'All':
            return '*'
        elif name in priority:
            return priority[name]
        else:
            return "Incorrect Data"

    def tracker(self, name):
        tracker = {'Bug': '1', 'Feature': '2', 'Support': '3', 'Misc': '4', 'Plan': '5',
                   'Improvement': '6', 'Test Case': '7'}

        if name == 'All':
            return '*'
        elif name in tracker:
            return tracker[name]
        else:
            return "Incorrect Data"

    def project(self, name):
        project = {'PatentCloud': '79', 'Shield': '150', 'TSD-Desktop v2.9.1': '170',
                   'TSD-Shield v2.7.0.1001': '171', 'Desktop RD item - v2.9.2': '179', 'TSD-Desktop v2.9.2': '190',
                   'Desktop RD item - v2.10.0': '194'}

        if name == 'All':
            return '*'
        elif name in project:
            return project[name]
        else:
            return "Incorrect Data"

    def fixedver(self, name):
        fixedver = {'2.7': '215', '2.8': '213', '2.9': '225', '3.0': '227'}

        if name =='All':
            return '*'
        elif name in fixedver:
            return fixedver[name]
        else:
            return "Incorrect Data"

    def user(self, name):
        user = {'Wayne': '492', 'Jason': '494', 'Kimi': '507', 'Willy': '530', 'Hubert': '545',
                  'Ramos': '556', 'Allen': '557', 'David': '559', 'Winny': '575', 'Siang': '576'}

        if name == 'All':
            return '*'
        elif name in user:
            return user[name]
        else:
            return "Incorrect Data"


class Num2Name:
    def status(self,id):
        status = {'1': 'New', '2': 'In Progress', '3': 'Resolved', '4': 'Feedback', '5': 'Closed', '6': 'Rejected',
                  '8': 'Request More Info', '9': 'Request More Info', '11': 'Cancel', '12': 'Cancel', '13': 'Assigned',
                  '14': 'Failed', '15': 'Obsolete', '16': 'Known Issue'}

        if id == '*':
            return 'All'
        elif id in status:
            return status[id]
        else:
            return "Incorrect Data"

    def priority(self, id):
        priority = {'3': 'P4', '4': 'P3', '5': 'P2', '6': 'P0', '7': 'P1'}

        if id == '*':
            return 'All'
        elif id in priority:
            return priority[id]
        else:
            return "Incorrect Data"

    def tracker(self, id):
        tracker = {'1': 'Bug', '2': 'Feature', '3': 'Support', '4': 'Misc', '5': 'Plan',
                   '6': 'Improvement', '7': 'Test Case'}

        if id == '*':
            return 'All'
        elif id in tracker:
            return tracker[id]
        else:
            return "Incorrect Data"

    def project(self, id):
        project = {'79': 'PatentCloud', '150': 'Shield', '170': 'TSD-Desktop v2.9.1',
                   '171': 'TSD-Shield v2.7.0.1001', '179': 'Desktop RD item - v2.9.2', '190': 'TSD-Desktop v2.9.2',
                   '194': 'Desktop RD item - v2.10.0'}

        if id == '*':
            return 'All'
        elif id in project:
            return project[id]
        else:
            return "Incorrect Data"

    def fixedver(self, id):
        fixedver = {'215': '2.7', '213': '2.8', '225': '2.9', '227.': '3.0'}

        if id =='*':
            return 'All'
        elif id in fixedver:
            return fixedver[id]
        else:
            return "Incorrect Data"

    def user(self, id):
        user = {'492': 'Wayne', '494': 'Jason', '507': 'Kimi', '530': 'Willy', '545': 'Hubert',
                  '556': 'Ramos', '557': 'Allen', '559': 'David', '575': 'Winny', '576': 'Siang'}

        if id == '*':
            return 'All'
        elif id in user:
            return user[id]
        else:
            return "Incorrect Data"


