from datetime import date, timedelta
actual_year = date.today().year
tienda = ("Paulo", "Oman", "Jefe", "Carlos")

def assign_saturdays(year):
   d = date(year, 1, 1)
   d += timedelta(days = 3 ) 
   while d.year == year:
      yield d
      d += timedelta(days = 7)

for d in assign_saturdays(actual_year):
   print(d)
   print(tienda[1])