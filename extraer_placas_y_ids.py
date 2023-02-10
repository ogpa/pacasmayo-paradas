from bs4 import BeautifulSoup


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def convertir_alias(alias):
    c = "-"
    pos_guion = alias.find(c)
    if pos_guion != -1:
        placa = alias[pos_guion-3:pos_guion+4]
    else:
        placa = alias
    return placa


def extraer_placas_y_ids(login):
    temp = []
    lista_ids = []
    lista_placas = []
    doc = BeautifulSoup(login, "html.parser")
    for s in doc.find_all(
            "select", {"name": "vnGestionConductor$cbConductoresPlaca"}):
        for o in s.find_all("option"):
            temp.append(o)
    # print(temp)
    for p in temp:
        #c = extraer_texto(p, 'value="', '"')
        lista_ids.append(p["value"])
        placa = convertir_alias(p.text)
        lista_placas.append(placa)
    # print(lista_codigos_placas)
    lista_ids = lista_ids[2:]
    lista_placas = lista_placas[2:]
    dict_ids_y_placas = {
        "id": lista_ids,
        "placa": lista_placas
    }
    # print(lista_ids)
    # print(lista_placas)
    scrape_filename = "scrape_data.html"

    with open(scrape_filename, "w", encoding="utf-8") as f:  # Descomentar para hacer primer request
        f.write(login)  # Descomentar para hacer primer request
    #lista_codigos_placas = lista_codigos_placas[:-1]

    # Extraer placas Pacasmayo

    return dict_ids_y_placas
