from login_hunter import login_hunter
from extraer_placas_y_ids import extraer_placas_y_ids
from extraer_placas import extraer_placas
from obtener_reporte_paradas import obtener_reporte_paradas

l = login_hunter()
dict_placas_y_ids = extraer_placas_y_ids(l[0])
lista_placa_cliente = extraer_placas(l[0])
df = obtener_reporte_paradas(l[1], dict_placas_y_ids, lista_placa_cliente)
# print(dict_placas_y_ids)
# print(lista_placa_cliente)
