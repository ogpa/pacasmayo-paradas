from datetime import datetime, timedelta

MAXIMO_RANGO_DIAS = 14


def fechas_rango_semana():
    # ahora = datetime.now()

    # dia_de_semana = ahora.weekday()

    # 0 es lunes
    # Lunes anterior

    # ultimo_lunes = ahora - timedelta(days=dia_de_semana)

    fecha_inicio = datetime(2023, 6, 5)
    fecha_final = datetime(2023, 6, 18)
    diferencia_dias_temp = fecha_final - fecha_inicio
    diferencia_dias = diferencia_dias_temp.days
    lista_fechas = []
    contador = 0
    helper = 0
    while diferencia_dias >= 0:
        fecha_1 = fecha_inicio + timedelta(days=contador * (MAXIMO_RANGO_DIAS + 1))
        fecha_1_strf = fecha_1.strftime("%d/%m/%Y")
        if fecha_1 + timedelta(days=MAXIMO_RANGO_DIAS) > fecha_final:
            fecha_2 = fecha_final
        else:
            fecha_2 = fecha_1 + timedelta(days=MAXIMO_RANGO_DIAS)

        fecha_2_strf = fecha_2.strftime("%d/%m/%Y")
        par = [fecha_1_strf, fecha_2_strf]
        lista_fechas.append(par)
        contador = contador + 1
        helper = helper + 1
        diferencia_dias = diferencia_dias - MAXIMO_RANGO_DIAS - 1
    print(lista_fechas)
    # lunes_inicio = ultimo_lunes - timedelta(days=7)
    # domingo_final = ultimo_lunes - timedelta(days=1)
    # domingo_final = domingo_final + timedelta(days=4)
    # lunes_inicio_str = lunes_inicio.strftime("%d/%m/%Y")
    # domingo_final_str = domingo_final.strftime("%d/%m/%Y")

    # print(lunes_inicio_str)
    # print(domingo_final_str)

    # Separar en grupos de 14

    return lista_fechas


# fechas_rango_semana()
