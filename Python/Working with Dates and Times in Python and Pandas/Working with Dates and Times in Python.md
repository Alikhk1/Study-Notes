- Python has special date class called 'date'.
- from datetime import date
- .weekday() ~ Counts from Monday = 0.
- .total_seconds()

---

#   1. Math with Dates :

	- from datetime import timedelta	
	- When you subtract/add dates you get a Time Delta Object. You can acesss it by => Delta.days
	- CREATE TIMEDELTA OBJECT : td = timedelta(weeks=1, days=29)

--- 
#   2. Turning Dates into Strings :

	
	- We want to convert dates to strings, when we want to: Print Results, Filename, CSV/Excel File.
	- date.isoformat() : Prints a string
	- date.strftime("Year is %Y") : Format your date output

---

#   3. Dates with Time :


	- from datetime import datetime
	- CREATE DATETIME : datetime = datetime(2016, 6, 1, HOURS(24), 60 MINUTES, 60 SECONDS, MICRO SECONDS) 
	- CAN ALSO USE KEYWORD ARGS : datetime(year=,month=,day=,hour=,minute=,second=,microsecond=)
	- Computers Usually use 24 hour time.
	- date.replace(minutes=,seconds=)


---

#   4. Turning Strings into Dates :


	- dt = datetime.strptime('STRING', "FORMAT STRING %m/%d/%Y %H:%M:%S")
	- NEED EXACT MATCH TO CONVERT STRING.
	- UNIX TIME: Many computers the datetime as number of seconds since 1st 1970.
	- READ UNIX TIME : dt = datetime.fromtimestamp(UNIXTIME)

---

#   5. UTC Offsets :

	- from datetime import timezone
	- ET = timezone(timedelta(hours=-5)) - US EASTERN TIME
	- dt = datetime(2017, 01, 01, 13,25,25, tzinfo= ET)
	- dt.astimezone(IST) - CONVERTS TO TIME ZONE
	- dt.replace(tzinfo=timezone.utc) - KEEPS SAME TIME, CHANGES LABEL


---
#   6. Time Zone Database :

	
	- from dateutil import tz
	- et = tz.gettz('Continent/City')

---
#   7. Reading Date and Time in Pandas :
	
	- pd.read_csv('abcd.csv', parse_dates=['Start date', 'End date'])
	OR
	- pd.to_datetime(rides['Start date'], format= "%Y-%m-%d %H:%M:%S")

	- RESAMPLE : rides.resample('M', on = 'Start date')['Duration'].mean()
	
	- NEW TIME ZONE : rides['Start date'].dt.tz_localize('Asia/Lahore', ambiguous='NaT') , .tz_convert => CHANGE TIME ZONE

	- DATETIME OPERATIONS: .dt.day_name()








