import locale
from datetime import datetime, timedelta
import win_unicode_console


win_unicode_console.enable()
locale.setlocale(locale.LC_ALL, "russian")

def print_today():
    dt_now = datetime.now()

    date_string = dt_now.strftime('%A %d %B %Y')
    print(date_string)


def print_yesterday():
    delta = timedelta(days=1)
    dt_now = datetime.now()
    dt_yesterday = dt_now - delta
    date_string = dt_yesterday.strftime('%A %d %B %Y')
    print(date_string)

print(datetime.now())

print_today()
print_yesterday()


datetime.strptime('01/01/17 12:10:03.234567','%m/%d/%y %H:%M:%S.%f')



