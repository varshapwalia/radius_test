import urllib2
import json
from datetime import datetime, timedelta, date

def search_git(search):
  try:
    search_dict = {}
    temp = 0
    page = 1
    total = 0
    total_24 = 0
    total_7days = 0

    result = search.split('/')
    user = result[-2]
    repo = result[-1]

    while True:
      string = "https://api.github.com/repos/%s/%s/issues?state=open&+user:mozilla&page=%s&per_page=100" % (user,repo, page)
      jsoned = json.load(urllib2.urlopen(string))
      temp = len(jsoned)
      page += 1
      total += temp
      if temp<100:
        temp = 0
        page = 1
        break

    #making timestamps
    temp_day = datetime.today()-timedelta(days=1)
    day = temp_day.strftime('%Y-%m-%dT%H:%M:%S%Z')
    temp_week = datetime.today()-timedelta(days=7)
    week = temp_week.strftime('%Y-%m-%dT%H:%M:%S%Z')

    #For within 24 hours
    while True:
      string = "https://api.github.com/repos/%s/%s/issues?since=%s?state=open&+user:mozilla&page=%s&per_page=100" % (user,repo,day,page)
      jsoned = json.load(urllib2.urlopen(string))
      temp = len(jsoned)
      page += 1
      total_24 += temp
      if temp<100:
        temp = 0
        page = 1
        break

    #For within 24 hours to 7 days

    while True:
      string = "https://api.github.com/repos/%s/%s/issues?since=%s?state=open&+user:mozilla&page=%s&per_page=100" % (user,repo,week,page)
      jsoned = json.load(urllib2.urlopen(string))
      temp = len(jsoned)
      page += 1
      total_7days += temp
      if temp<100:
        temp = 0
        page = 1
        break

      


    # Not PAGINATED CODE

    # #open within 24 hours
    # string_24 = ("https://api.github.com/repos/%s/%s/issues?since=%s?state=open&+user:mozilla&per_page=100" % (user,repo,day))
    # contents_24 = json.load(urllib2.urlopen(string_24))
    # total_24 = len(contents_24)

    # #open in last 7 days hours
    # string_7days = ("https://api.github.com/repos/%s/%s/issues?since=%s?state=open&+user:mozilla&per_page=100" % (user,repo,week))
    # contents_7days = json.load(urllib2.urlopen(string_7days))
    # total_7days = len(contents_7days)

    search_dict['total'] = total
    search_dict['within_24hrs'] = total_24
    search_dict['24hrs_to_7days'] = total_7days - total_24
    search_dict['beyond_7days'] = total - total_7days

    return search_dict
    
  except Exception as e:
    print e
