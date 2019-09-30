from django.shortcuts import render
 # from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099:
        year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    announcements = [
        {
            'date': '8-10-2019', 'announcement': "Club Registrations Open"
        },
        {
            'date': '8-15-2019', 'announcement': "Joe Smith Elected New Club President"
        }
    ]
    return render(request, 'templating/index.html', {'title': title, 'cal': cal, 'announcements': announcements})