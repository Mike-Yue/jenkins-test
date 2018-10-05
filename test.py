import datetime
from dateutil import tz

if __name__ == "__main__":
	print(datetime.date.today())
	utc = datetime.datetime.now()
	my_zone = tz.tzlocal()
	real_time = utc.replace(tzinfo=my_zone)
	print real_time