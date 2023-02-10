HUN_CAB_COOKIE = "ASP.NET_SessionId="
HUN_FIN_COOKIE = "; path=/;"
HUN_CAB_VIEWSTATE = 'id="__VIEWSTATE" value="'
HUN_FIN_VIEWSTATE = '"'
HUN_CAB_VIEWSTATEGENERATOR = 'id="__VIEWSTATEGENERATOR" value="'
HUN_FIN_VIEWSTATEGENERATOR = '"'
HUN_CAB_EVENTVALIDATION = 'id="__EVENTVALIDATION" value="'
HUN_FIN_EVENTVALIDATION = '"'
HUN_CAB_TXLATITUDMAPA = 'id="txLatitudMapa" value="'
HUN_FIN_TXLATITUDMAPA = '"'
HUN_CAB_TXLONGITUDMAPA = 'id="txLongitudMapa" value="'
HUN_FIN_TXLONGITUDMAPA = '"'
HUN_CAB_TXMARCADOR = 'id="txMarcador" value="'
HUN_FIN_TXMARCADOR = '"'
HUN_CAB_HDWUID = 'id="hdwuid" value="'
HUN_FIN_HDWUID = '"'
HUN_CAB_GRDPARADAS = 'id="grdParadas_State" value="'
HUN_FIN_GRDPARADAS = '"'
# cookie,viewstate,viewstategenerator,eventvalidation


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def extraer_datos_session(response):
    cookie = extraer_texto(
        response.headers["Set-Cookie"], HUN_CAB_COOKIE, HUN_FIN_COOKIE)
    # print(cookie_LogIn)

    viewstate = extraer_texto(
        response.text, HUN_CAB_VIEWSTATE, HUN_FIN_VIEWSTATE)
    # print(viewstate_LogIn)

    viewstategenerator = extraer_texto(
        response.text, HUN_CAB_VIEWSTATEGENERATOR, HUN_FIN_VIEWSTATEGENERATOR)
    # print(viewstategenerator_LogIn)

    eventvalidation = extraer_texto(
        response.text, HUN_CAB_EVENTVALIDATION, HUN_FIN_EVENTVALIDATION)
    # print(eventvalidation_LogIn)

    txLatitudMapa = extraer_texto(
        response.text, HUN_CAB_EVENTVALIDATION, HUN_FIN_EVENTVALIDATION)
    # print(eventvalidation)
    return cookie, viewstate, viewstategenerator, eventvalidation
