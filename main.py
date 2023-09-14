from datetime import datetime, timedelta
import calendar
mes = datetime.now().month-1
mes2 = str(mes).zfill(2)
ano = datetime.now().year
dia = calendar.monthrange(ano, mes)[1]
print(dia)
