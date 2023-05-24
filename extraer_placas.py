from bs4 import BeautifulSoup
import pandas as pd


def convertir_alias(alias):
    c = "-"
    pos_guion = alias.find(c)
    if pos_guion != -1:
        placa = alias[pos_guion - 3 : pos_guion + 4]
    else:
        placa = alias
    return placa


# ruta = "scrape_data.html"
# doc = BeautifulSoup(
#     open(ruta, "r", encoding="utf-8"), "html.parser")


def extraer_placas(login):
    doc = BeautifulSoup(login, "html.parser")
    # print(doc(string=lambda s: "MB RENTING PACASMAYO " in s.text))
    a = doc(string=lambda s: "MB RENTING SA (" in s.text)
    # Se asume que solo encontrará 1
    for s in doc.find_all("a", string=a[0]):
        id_nodo = s["id"]
    # Con el nodo buscar todas sus placas
    # Ejemplo nodo: trvUnidades310
    nodo = id_nodo.replace("Unidadest", "Unidadesn") + "Nodes"
    # print(nodo)

    div_cliente_nodo = doc.find_all("div", {"id": nodo})
    # print(len(div_pacasmayo)) # 1
    # print(div_pacasmayo)

    lista_placa_cliente = []
    for div in div_cliente_nodo:
        for td in div.find_all("td", {"style": "white-space:nowrap;"}):
            placa = convertir_alias(td.text)
            lista_placa_cliente.append(placa)
    return lista_placa_cliente
