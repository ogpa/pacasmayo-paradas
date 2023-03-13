from datetime import datetime, timedelta


def fechas_rango_semana():
    ahora = datetime.now()

    dia_de_semana = ahora.weekday()

    # 0 es lunes
    # Lunes anterior

    ultimo_lunes = ahora - timedelta(days=dia_de_semana)

    lunes_inicio = ultimo_lunes - timedelta(days=7)
    domingo_final = ultimo_lunes - timedelta(days=1)
    #domingo_final = domingo_final + timedelta(days=4)
    lunes_inicio_str = lunes_inicio.strftime("%d/%m/%Y")
    domingo_final_str = domingo_final.strftime("%d/%m/%Y")

    print(lunes_inicio_str)
    print(domingo_final_str)

    return lunes_inicio_str, domingo_final_str
