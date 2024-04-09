import json
import requests

# Obtiene el indicador solicitado


def obtenerIndicadores():
    # Obtiene el valor actual de los indicadores [uf, ivp, dolar, dolar_intercambio, euro, ipc, utm, imacec, tpm, libra_cobre, tasa_desempleo, bitcoin]
    url = f'https://mindicador.cl/api/'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    # Para que el json se vea ordenado, retornar pretty_json
    pretty_json = json.dumps(data, indent=2)
    return data


# Se genera una lista con indicadores para iterar.
json_data = obtenerIndicadores()

indicadores = ["uf", "ivp", "dolar", "dolar_intercambio", "euro", "ipc",
               "utm", "imacec", "tpm", "libra_cobre", "tasa_desempleo", "bitcoin"]

# Muestra todos los indicadores rescatados de la consulta.
for indicador in indicadores:
    print(json_data[indicador])


# ENTREGA LA INFORMACION CORRESPONDIENTE A 30 DIAS HACIA ATRAS
def obtenerIndicador(indicador):
    url = f'https://mindicador.cl/api/{indicador}'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    # Para que el json se vea ordenado, retornar pretty_json
    pretty_json = json.dumps(data, indent=2)
    return data


info_indicador = json.dumps(obtenerIndicador("uf"), indent=2)

print(info_indicador)


# CONSULTA EL VALOR DE UN INDICADOR DADA UNA FECHA DETERMINADA

fecha = "17-12-1993"  # DEBE IR EN ESTE FORMATO
tipo_indicador = "uf"


def obtenerIndicadorFecha(tipo_indicador, fecha):
    url = f'https://mindicador.cl/api/{tipo_indicador}/{fecha}'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    # Para que el json se vea ordenado, retornar pretty_json
    pretty_json = json.dumps(data, indent=2)
    return data


print(obtenerIndicadorFecha(tipo_indicador, fecha))

tipo_indicador = "uf"
anio = '1990'


# Obtiene los valores del indicador un año determinado.

def obtenerIndicadorAño(tipo_indicador, anio):
    url = f'https://mindicador.cl/api/{tipo_indicador}/{anio}'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    # Para que el json se vea ordenado, retornar pretty_json
    pretty_json = json.dumps(data, indent=2)
    return data


print(json.dumps(obtenerIndicadorAño(tipo_indicador, anio), indent=2))
