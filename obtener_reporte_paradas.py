import requests
import pandas as pd
from urllib.parse import quote
from fechas_rango_semana import fechas_rango_semana
from extraer_datos_session_paradas import extraer_datos_session_paradas
from procesar_excel import procesar_excel

URL_BASE_REPORTE_PARADAS = (
    "http://www.huntermonitoreoperu.com/GeoV3.3/Paginas/Recorrido.aspx?"
)
URL_MAIN36 = "http://www.huntermonitoreoperu.com/GeoV3.3/Paginas/Main36.aspx"
URL_DESCARGAR_EXCEL = ""
MINIMO_MINUTOS = "20"


def reporte_unitario(id_placa, placa, cookie, fecha_inicio, fecha_fin):
    # Las fechas son en formato dd/mm/yyyy
    url = (
        URL_BASE_REPORTE_PARADAS
        + "ID="
        + id_placa
        + "&P="
        + placa
        + "&I=CUS&T=RRP&INI="
        + fecha_inicio
        + "%2000:00:00&FIN="
        + fecha_fin
        + "%2023:00:59&PTO=0&MIN="
        + MINIMO_MINUTOS
        + "&CRI=1&FHS=0"
    )

    payload = {}
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "ASP.NET_SessionId=" + cookie,
        "Referer": URL_MAIN36,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    d_Response = extraer_datos_session_paradas(response)

    # c_Response = d_Response[0]
    vs_Response = d_Response[1]
    vsg_Response = d_Response[2]
    ev_Response = d_Response[3]
    txlat_Response = d_Response[4]
    txlon_Response = d_Response[5]
    txmarc_Response = d_Response[6]
    hdwuid_Response = d_Response[7]
    grdpar_Response = d_Response[8]
    txlatini_Response = d_Response[9]
    txlonini_Response = d_Response[10]

    url_Excel = url
    payload_Excel = (
        "__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE="
        + quote(vs_Response, safe="")
        + "&__VIEWSTATEGENERATOR="
        + quote(vsg_Response, safe="")
        + "&__EVENTVALIDATION="
        + quote(ev_Response, safe="")
        + "&txLatitudMapa="
        + quote(txlat_Response, safe="")
        + "&txLongitudMapa="
        + quote(txlon_Response, safe="")
        + "&txEA1=&txEA2=&txEA3=&txSteps=false&txMarcador="
        + quote(txmarc_Response, safe="")
        + "&txMostrarCoordenadas=&hdpais=PE&txCapasAdicionales=&hdtiporeporte=RRP&hdservidorpe=http%3A%2F%2F190.223.20.10&hdservidorpex=http%3A%2F%2F190.223.20.10%3A8080&hdservidorcapaspe=http%3A%2F%2F190.223.20.10%3A8080&hdlistamapas=OS%2CGM%2CHUN%2CIOS&hdwuid="
        + quote(hdwuid_Response, safe="")
        + "&hddistancia=&hdcluster=false&imgExcel.x=10&imgExcel.y=20&tbGrafico=%7B%26quot%3BactiveTabIndex%26quot%3B%3A0%7D&grdParadas="
        + quote(grdpar_Response, safe="")
        + "&txContador=53&txMaxRegistrosRecorrido=5000&txContadorPuntos=&vnMensajeState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnPuntosReferencialRState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&hdpuntos=&hdusuario=20605414410&hdnombreusuario=MB%2BRENTING%2BPACASMAYO&hdidusuario=93084&hdvid="
        + id_placa
        + "&hdcolumna=&hddesde="
        + quote(fecha_inicio, safe="")
        + "%2B00%3A00%3A00&hdhasta="
        + quote(fecha_fin, safe="")
        + "%2B23%3A00%3A59&hdmotormapa=GM&txLatitudInicial="
        + quote(txlatini_Response, safe="")
        + "&txLongitudInicial="
        + quote(txlonini_Response, safe="")
        + "&txUnidadVelocidad=Km%2FH&hdappid=&hdappcode=&txZoom=10&hdintervalo=CUS&hdsecuenciarep=&hdmostrarnv=1&hdflechas=0&hdexisteimagen=&hdurlimagen=http%3A%2F%2Fwww.huntermonitoreoperu.com%2Fstaticmap%2Fmapar.php&hdarchivoi=&hddestinoi=&DXScript=1_11%2C1_252%2C1_12%2C1_23%2C1_64%2C1_14%2C1_15%2C1_49%2C1_24%2C1_43%2C1_182%2C1_19%2C1_213%2C1_224%2C1_225%2C1_212%2C1_214%2C1_222%2C1_223%2C1_211%2C1_227%2C1_236%2C1_238%2C1_239%2C1_226%2C1_231%2C1_233%2C1_230%2C1_234%2C1_240%2C1_183%2C1_184%2C1_42%2C1_17%2C1_41&DXCss=1_68%2C1_69%2C0_629%2C1_209%2C0_5143%2C0_2771%2C0_2776%2C0_5138%2C1_254%2C1_74%2C1_253%2C1_73%2C1_210%2C1_207%2C1_206"
    )
    # payload_Excel = quote(payload_Excel, safe="")
    # print(payload_Excel)
    headers_Excel = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "ASP.NET_SessionId=" + cookie,
        "Origin": "http://www.huntermonitoreoperu.com",
        "Referer": url,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }

    response_Excel = requests.request(
        "POST", url_Excel, headers=headers_Excel, data=payload_Excel
    )
    nombreArchivo_Paradas = "paradas_hunter.xlsx"
    fo = open(nombreArchivo_Paradas, "wb")
    open(nombreArchivo_Paradas, "wb").write(response_Excel.content)
    fo.close()
    return nombreArchivo_Paradas


# def procesar_excel(ruta_archivo_paradas):
#     df = pd.read_excel(ruta_archivo_paradas)
#     df = df[3:]
#     return df


def obtener_reporte_paradas(cookie, dict_placas_y_ids, lista_placa_cliente):
    # Estoy omitiendo el request que se hace cuando se escoge la placa en el label "Unidad"

    # Con la placa (de lista placa) obtener el id de dict placa id
    fechas = (
        fechas_rango_semana()
    )  # Ejemplo: [['01/05/2023', '15/05/2023'], ['16/05/2023', '16/05/2023']]
    # print(dict_placas_y_ids)
    # print(lista_placa_cliente)
    # for placa in lista_placa_cliente:
    #     index = dict_placas_y_ids["placa"].index(placa)
    #     id_placa = dict_placas_y_ids["id"][index]
    #     df = reporte_unitario(id_placa, placa, cookie, fechas[0], fechas[1])
    # lista_dfs = []
    #lista_original = ["BLV-785"]  # Modificado 24/05/2023
    # Usen esta lista si quieren tomar en cuenta solo ciertas placas
    # Si quieren que salgan todas, comentar línea de lista_orignal y "if placa in lista_original"
    lista_total = []
    for par_fechas in fechas:
        for placa in lista_placa_cliente:
            # placa = lista_placa_cliente[0]
            #if placa in lista_original:  # Modificado 24/05/2023
                index = dict_placas_y_ids["placa"].index(placa)
                id_placa = dict_placas_y_ids["id"][index]
                print(placa)
                print(id_placa)
                ruta_archivo_paradas = reporte_unitario(
                    id_placa, placa, cookie, par_fechas[0], par_fechas[1]
                )

                # Retorna el df de una placa
                df = procesar_excel(ruta_archivo_paradas, placa)

                # lista_dfs.append(df)
                lista_total.append(df)
            # df_total = pd.merge(df_total, df)
        # lista_total.append(lista_dfs)
    # print(df)
    # return x
    # df_total = pd.concat(lista_dfs)
    df_total = pd.concat(lista_total)
    df_total.to_csv("total.csv", index=False)
