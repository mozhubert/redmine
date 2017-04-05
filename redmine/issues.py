# -*- coding: utf8 -*-

import requests
import json
import config

class Info:
    def amount(self, url):
        CheckURL = requests.get(url)
        doc = json.loads(CheckURL.text)

        return doc['total_count']

    def list(self, url):
        CheckURL = requests.get(url)
        doc = json.loads(CheckURL.text)

        if doc['total_count'] > 0:
            for i in range(0, (doc['total_count']/25)+1):
                NewURL = url + '&offset={}'.format(i*25)
                CheckURL = requests.get(NewURL)
                doc = json.loads(CheckURL.text)

                for j in range(0, len(doc['issues'])):
                    issue = doc['issues'][j]
                    print issue['id'],
                    print issue['priority']['name'],
                    print issue['subject']
        else:
            print "Without any issue"
            return False

    def idlist(self, url):
        CheckURL = requests.get(url)
        doc = json.loads(CheckURL.text)

        if doc['total_count'] > 0:
            idlist = []

            for i in range(0, (doc['total_count'] / 25) + 1):
                NewURL = url + '&offset={}'.format(i*25)
                print NewURL
                CheckURL = requests.get(NewURL)
                doc = json.loads(CheckURL.text)

                for j in range(0, len(doc['issues'])):
                    idlist.append(doc['issues'][j]['id'])
            return idlist
        else:
            print "Without any issue"
            return False