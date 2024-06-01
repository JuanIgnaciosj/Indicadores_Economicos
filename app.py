"""
    ESTE SCRIPT ES UNA IMPLEMENTACION SIMPLE DE LA API ALOJADA EN https://mindicador.cl/

    LA IMPLEMENTACION ACTUAL CONSISTE EN CONSULTAS SIMPLES QUE SERAN EJECUTADAS POR UN BOT DE TELEGRAM
    -- EN DESARROLLO --
    Returns:
        _type_: _description_
    """


# Listado de indicadores disponibles
import requests
import json

indicadores = ["uf", "ivp", "dolar", "dolar_intercambio", "euro", "ipc",
               "utm", "imacec", "tpm", "libra_cobre", "tasa_desempleo", "bitcoin"]


# Convertirlo en una API que pueda llamar los metodos

# Funcion 1 del Bot: OBTIENE EL PRECIO LISTADO EN LA
# def obtenerIndicadores():
#     # Obtiene el valor actual de los indicadores [uf, ivp, dolar, dolar_intercambio, euro, ipc, utm, imacec, tpm, libra_cobre, tasa_desempleo, bitcoin]
#     url = f'https://mindicador.cl/api/'
#     response = requests.get(url)
#     data = json.loads(response.text.encode("utf-8"))
#     # Para que el json se vea ordenado, retornar pretty_json
#     # pretty_json = json.dumps(data, indent=2)
#     return data


# # Se genera una lista con indicadores para iterar.
# json_data = obtenerIndicadores()

# # Muestra todos los indicadores rescatados de la consulta formateados de forma facil de leer
# print("Los valores son mostrados a la fecha: " + json_data['fecha'][:10])

# # Itera y muestra los indicadores
# for indicador in indicadores:
#     # json_data[indicador]
#     # print(json_data[indicador])
#     if (json_data[indicador]['nombre'] in ('Indice de Precios al Consumidor (IPC)', 'Imacec', 'Tasa de desempleo', 'Tasa Política Monetaria (TPM)')):
#         print("El valor de " + json_data[indicador]['nombre'] + " corresponde a " +
#               str((json_data[indicador]['valor'])) + " %")  # + json_data[indicador]['unidad_medida'])
#     elif (json_data[indicador]['nombre'] in ('Unidad de fomento (UF)', 'Indice de valor promedio (IVP)', 'Dólar observado', 'Dólar acuerdo', 'Euro', 'Unidad Tributaria Mensual (UTM)')):
#         print("El valor de " + json_data[indicador]['nombre'] + " corresponde a " +
#               "$ "+str('{:,}'.format(json_data[indicador]['valor']).replace(',', '.')) + " " + json_data[indicador]['unidad_medida'])
#     else: # SON TODOS LOS INDICADORES CON VALOR EN DOLAR
#         print("El valor de " + json_data[indicador]['nombre'] + " corresponde a " +
#               "U$ "+str(json_data[indicador]['valor']) + " " + json_data[indicador]['unidad_medida'])
# HASTA ACA LLEGA LA PRIMERA FUNCION DEL BOT


# -----------------------SEGUNDA FUNCION DEL BOT

# ENTREGA LA INFORMACION CORRESPONDIENTE A 30 DIAS HACIA ATRAS DADO UN INDICADOR ESPECIFICO.


# def obtenerIndicador(indicador):
#     url = f'https://mindicador.cl/api/{indicador}'
#     response = requests.get(url)
#     data = json.loads(json.dumps(json.loads(
#         response.text.encode("utf-8")), indent=2))
#     # Para que el json se vea ordenado, retornar pretty_json
#     # pretty_json = json.dumps(data, indent=2)
#     return data

# info_indicador = obtenerIndicador("uf")

# #Obtiene nombre de la estadistica consultada
# print(info_indicador['nombre'])  # el label a obtener es nombre

# #Obtiene el valor diario por los ultimos 30 dias
# print(info_indicador['serie'])

# PUNTOS A CONSIDERAR PARA PROGRAMAR
# GRAFICAR EL VALOR DE LOS ULTIMOS 30 DIAS Y RETORNAR UNA FOTO
# GRAFICAR LA MEDIA (O EL VALOR A LA MITAD DEL MES)
# FORMATEAR BIEN EL GRAFICO
# RETORNAR LO ANTERIOR COMO MENSAJE POR MEDIO DE UN MENSAJE DEL BOT

# --------------------- AQUI TERMINA LA SEGUNDA FUNCION DEL BOT DE PYTHON --


# Solo obtiene la informacion de los valores de los ultimos 30 dias
# for label in info_indicador.keys():
#     print(info_indicador.key())
#     print('\n')
#     print(info_indicador[label])
#     ## Entrega el valor del indicador especificado para los ultimos 30 dias


# # CONSULTA EL VALOR DE UN INDICADOR DADA UNA FECHA DETERMINADA
# CONSIDERAR DOS FUNCIONES DESDE ESTA YA QUE PUEDEN SER TODOS LOS INDICADORES O UNA CONSULTA POR UNO EN ESPECIFICO


# fecha = "17-12-2012"  # DEBE IR EN ESTE FORMATO
# tipo_indicador = "uf"


# def obtenerIndicadorFecha(tipo_indicador, fecha):
#     url = f'https://mindicador.cl/api/{tipo_indicador}/{fecha}'
#     response = requests.get(url)
#     data = json.loads(json.dumps(json.loads(
#         response.text.encode("utf-8")), indent=2))
#     # Para que el json se vea ordenado, retornar pretty_json
#     # pretty_json = json.dumps(data, indent=2)
#     return data


# print(obtenerIndicadorFecha(tipo_indicador, fecha))

# # LA MISMA FUNCION PERO ITERABLE

# for label in indicadores:
#     print("La fecha consultada para el valor de "+ label + "corresponde a:"+fecha))
#     if (obtenerIndicadorFecha(label, fecha)['nombre'] in ('Indice de Precios al Consumidor (IPC)', 'Imacec', 'Tasa de desempleo', 'Tasa Política Monetaria (TPM)')):
#         print("El valor de " + obtenerIndicadorFecha(label, fecha)['nombre'] + " corresponde a " +
#               str(obtenerIndicadorFecha(label, fecha)['serie'][0]['valor']) + " %")
#     elif obtenerIndicadorFecha(label, fecha)['nombre'] in ('Unidad de fomento (UF)', 'Indice de valor promedio (IVP)', 'Dólar observado', 'Dólar acuerdo', 'Euro', 'Unidad Tributaria Mensual (UTM)'):
#         print("El valor de " + obtenerIndicadorFecha(label, fecha)['nombre'] + " corresponde a " +
#               "$ "+str('{:,}'.format(obtenerIndicadorFecha(label, fecha)['serie'][0]['valor']).replace(',', '.')) + " " + obtenerIndicadorFecha(label, fecha)['unidad_medida'])
#     else:  # SON TODOS LOS INDICADORES CON VALOR EN DOLAR
#         print("El valor de " + obtenerIndicadorFecha(label, fecha)['nombre'] + " corresponde a " +
#               "U$ "+str(obtenerIndicadorFecha(label, fecha)['serie'][0]['valor']) + " " + obtenerIndicadorFecha(label, fecha)['unidad_medida'])


# COSAS PENDIENTES
# FORMATEAR LAS SALIDAS DE LOS VALORES COMO LA PRIMERA FUNCION
# EL INGRESO DE LA VARIABLE DEBE VENIR DESDE EL MENSAJE DEL TELEGRAM (HACER TAMBIEN LA VERSION DE INGRESO POR CONSOLA DE PYTHON)
# Evitar que se caiga cuand consulta por el btc desde una cierta fecha. (Aqui verificar cual es la minima fecha que tiene disponible y hacer la validacion)


# ---- HASTA AQUI LA TERCERA FUNCION DEL BOT

# --- Aqui comienza la 4ta funcion del bot --

tipo_indicador = "uf"
anio = '1990'

# Obtiene los valores del indicador un año determinado.

# Considerar tambien las validaciones de los activos que no tienen valor un año determinado


def obtenerIndicadorAño(tipo_indicador, anio):
    url = f'https://mindicador.cl/api/{tipo_indicador}/{anio}'
    response = requests.get(url)
    data = json.dumps(json.loads(response.text.encode("utf-8")), indent=2)
    # Para que el json se vea ordenado, retornar pretty_json
    # pretty_json = json.dumps(data, indent=2)
    return data


print(obtenerIndicadorAño(tipo_indicador, anio))+

# Cosas que faltan formatear
# Considerar que se muestre el nombre, año y los valores
# armar un grafico con el valor del ultimo año
# Retornar la foto en el mensaje que vuelve hacia el telegram.
