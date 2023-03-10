import datetime

fecha = "Mar 5 2023"
num_dia = datetime.datetime.strptime(fecha, "%b %d %Y").weekday()
nueva_fecha = datetime.datetime.strptime(fecha, "%b %d %Y")
nueva_fecha = nueva_fecha.strftime("%d/%m/%Y")
print(nueva_fecha)
