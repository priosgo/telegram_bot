import gspread
import time
from login import login
import datetime
from date_parser import week_day

FILE_NAME = 'Sales_2020_1st'


def get_sheets_sales(fecha):
    
    try:
        sales = login(FILE_NAME)    
        date_sheet = sales.worksheet(fecha)
        try:
            wday = week_day(fecha)
            compras = date_sheet.acell('F1').value
            time.sleep(1)
            venta_total = date_sheet.acell('L1').value
            time.sleep(1)
            day_sale = [wday, compras, venta_total]
            return day_sale
        except:
            return'No fue posible encontrar  la informacion...'
    except Exception as err:
        return err
