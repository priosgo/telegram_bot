import datetime
LUNES = 'Lunes'
MARTES = 'Martes'
MIERCOLES = 'Miercoles'
JUEVES = 'Jueves'
VIERNES = 'Viernes'
SABADO = 'Sabado'
DOMINGO = 'Domingo'
ENERO = 'Enero'
FEBRERO = 'Febrero'
MARZO = 'Marzo'
ABRIL = 'Abril'
MAYO = 'Mayo'
JUNIO = 'Junio'
JULIO = 'Julio'
AGOSTO = 'Agosto'
SEPTIEMBRE = 'Septiembre'
OCTUBRE = 'Octubre'
NOVIEMBRE = 'Noviembre'
DICIEMBRE = 'Diciembre'
NOT_FOUND = 'Invalid date'
NOT_FOUND_M = 'Invalid month'

def week_day(date):
    day = int(date[0:2])
    month = int(date[3:5])
    year = int('20' + date[6:8])
    week_day = datetime.date(year, month, day).weekday()
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