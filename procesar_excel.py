import pandas as pd
import datetime
import openpyxl

#ruta_archivo_paradas = "paradas_hunter.xlsx"

CABECERA_LATITUD_HIPER = 'http://maps.google.com/maps/api/staticmap?zoom=18&size=512x512&maptype=roadmap&markers=color:red%7Clabel:C%7C'
FIN_LATITUD_HIPER = ','
CABECERA_LONGITUD_HIPER = ','
FIN_LONGITUD_HIPER = '&sensor=false&center='


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def convertir_fechas(fecha_hora_string):
    fecha_hora_string = fecha_hora_string + "x"
    fecha = fecha_hora_string[:10]
    #fecha_hora_string = str(fecha_hora_string)
    #hora = fecha_hora_string[-8:]
    hora = extraer_texto(fecha_hora_string, " ", "x")
    num_dia = datetime.datetime.strptime(fecha, "%d/%m/%Y").weekday()
    # 0 es domingo
    if num_dia == 0:
        dia = "Lunes"
    elif num_dia == 1:
        dia = "Martes"
    elif num_dia == 2:
        dia = "Miercoles"
    elif num_dia == 3:
        dia = "Jueves"
    elif num_dia == 4:
        dia = "Viernes"
    elif num_dia == 5:
        dia = "Sabado"
    elif num_dia == 6:
        dia = "Domingo"
    # return fecha, hora, dia
    return dia


def convertir_fechas_v2(fecha_hora_string):
    fecha_hora_string = fecha_hora_string + "x"
    fecha = fecha_hora_string[:10]
    num_dia = datetime.datetime.strptime(fecha, "%d/%m/%Y").weekday()
    # 0 es domingo
    if num_dia == 0:
        dia = "Lunes"
    elif num_dia == 1:
        dia = "Martes"
    elif num_dia == 2:
        dia = "Miercoles"
    elif num_dia == 3:
        dia = "Jueves"
    elif num_dia == 4:
        dia = "Viernes"
    elif num_dia == 5:
        dia = "Sabado"
    elif num_dia == 6:
        dia = "Domingo"
    # return fecha, hora, dia
    return dia


def convertir_hora(fecha_hora_string):
    hora = extraer_texto(fecha_hora_string, " ", "x")
    hora_final = extraer_texto(hora, "", ":")
    return hora_final


def rango_hora(desde_hora, desde_dia_de_la_semana):
    int_desde_hora = int(desde_hora)
    if (desde_dia_de_la_semana == "Sabado") or (desde_dia_de_la_semana == "Domingo") or (int_desde_hora < 5) or (int_desde_hora >= 19):
        rango = "Fuera de horario laboral"
    else:
        rango = "Dentro de horario laboral"
    return rango


def convertir_latitud_longitud(hipervinculo):
    latitud = extraer_texto(
        hipervinculo, CABECERA_LATITUD_HIPER, FIN_LATITUD_HIPER)
    longitud = extraer_texto(
        hipervinculo, CABECERA_LONGITUD_HIPER, FIN_LONGITUD_HIPER)
    return latitud, longitud

# Extraer latitud y longitud de hipervinculo


def procesar_excel(ruta_archivo_paradas, placa):
    wb = openpyxl.load_workbook(ruta_archivo_paradas)
    ws = wb["Sheet"]

    lista_latitud = []
    lista_longitud = []
    # min_col = 4 y max_col = 4 porque los hipervínculos están en la columna 4
    for x in ws.iter_rows(min_col=4, max_col=4, min_row=4):
        # print(x)
        # Agrego "x" para que sea fácil encontrarlo
        hipervinculo = x[0].hyperlink.target
        coordenadas = convertir_latitud_longitud(hipervinculo)
        lista_latitud.append(coordenadas[0])
        lista_longitud.append(coordenadas[1])

    dict_coordenadas = {
        "Latitud": lista_latitud,
        "Longitud": lista_longitud
    }
    df_coordenadas = pd.DataFrame(dict_coordenadas)

    # Procesar excel

    df = pd.read_excel(ruta_archivo_paradas)
    df = df[1:]
    df.columns = df.iloc[0]
    # df.iloc[pd.RangeIndex(len(df)).drop(1)]
    df = df[1:]
    # df.drop(df.index[0])
    if df.empty == False:
        # print(df)
        # df.drop([1])
        # print(df)
        #df.columns = range(df.shape[1])
        print(df.columns)
        df = df[["Desde", "Hasta", "Duración", "Calle", "Kilometraje"]]
        #df = df.iloc[:, [0, 1, 2, 3, 7]]
        df.columns = range(df.shape[1])
        #df.to_csv("hola.csv", index=False)
        df = df.rename(
            columns={df.columns[0]: "Desde", df.columns[1]: "Hasta", df.columns[2]: "Duracion parada (hh:mm:ss)", df.columns[3]: "Calle", df.columns[4]: "Kilometraje"})

        # Desde fecha
        # Desde hora
        # Hasta fecha
        # Hasta hora
        # Desde día
        # latitud
        # longitud

        # df[["Desde (fecha)", "Desde (hora)", "Desde (dia)"]] = df.apply(
        #    lambda x: convertir_fechas(x["Desde"]), axis='columns', result_type='expand')
        # df[["Hasta (fecha)", "Hasta (hora)", "Hasta (dia)"]] = df.apply(
        #    lambda x: convertir_fechas(x["Hasta"]), axis='columns', result_type='expand')
        df["Desde (dia de la semana)"] = df.apply(
            lambda x: convertir_fechas_v2(x["Desde"]), axis='columns')
        df["Hasta (dia de la semana)"] = df.apply(
            lambda x: convertir_fechas_v2(x["Hasta"]), axis='columns')

        df["Desde (hora)"] = df.apply(
            lambda x: convertir_hora(x["Desde"]), axis='columns')
        df["Hasta (hora)"] = df.apply(
            lambda x: convertir_hora(x["Hasta"]), axis='columns')
        df = pd.merge(df, df_coordenadas, left_index=True, right_index=True)
        df["Rango"] = df.apply(lambda x: rango_hora(
            x["Desde (hora)"], x["Desde (dia de la semana)"]), axis='columns')
        #df.to_csv("final.csv", index=False)
        # print(df)
        df["Placa"] = placa
        return df
