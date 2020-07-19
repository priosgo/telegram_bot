import datetime

LUNES = 'Monday'
MARTES = 'Tuesday'
MIERCOLES = 'Wednesday'
JUEVES = 'Thursday'
VIERNES = 'Friday'
SABADO = 'Saturday'
DOMINGO = 'Sunday'
ENERO = 'January'
FEBRERO = 'February'
MARZO = 'March'
ABRIL = 'April'
MAYO = 'May'
JUNIO = 'June'
JULIO = 'July'
AGOSTO = 'August'
SEPTIEMBRE = 'September'
OCTUBRE = 'Octuber'
NOVIEMBRE = 'November'
DICIEMBRE = 'December'
NOT_FOUND = 'Invalid date'
NOT_FOUND_M = 'Invalid month'

def week_day(date):
    day = date.split('-')
    week_day = datetime.datetime(int('20'+day[2]), int(day[1]), int(day[0])).weekday()
    if week_day == 0:
        return LUNES
    elif week_day == 1:
        return MARTES
    elif week_day == 2:
        return MIERCOLES
    elif week_day == 3:
        return JUEVES
    elif week_day == 4:
        return VIERNES
    elif week_day == 5:
        return SABADO
    elif week_day == 6:
        return DOMINGO
    else:
        return NOT_FOUND

def month(date):
     month = int(date[3:5])
     if month == 1:
         return ENERO
     elif month == 2:
         return FEBRERO
     elif month == 3:
         return MARZO
     elif month == 4:
         return ABRIL
     elif month == 5:
         return MAYO
     elif month == 6:
         return JUNIO
     elif month == 7:
         return JULIO
     elif month == 8:
         return AGOSTO
     elif month == 9:
         return SEPTIEMBRE
     elif month == 10:
         return OCTUBRE
     elif month == 11:
         return NOVIEMBRE
     elif month == 12:
         return DICIEMBRE
     else:
         return NOT_FOUND_M