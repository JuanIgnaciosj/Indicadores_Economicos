"""
    ESTE SCRIPT ES UNA IMPLEMENTACION SIMPLE DE LA API ALOJADA EN https://mindicador.cl/

    LA IMPLEMENTACION ACTUAL CONSISTE EN CONSULTAS SIMPLES QUE SERAN EJECUTADAS POR UN BOT DE TELEGRAM
    -- EN DESARROLLO --
    LA IMPLEMENTACION CONSIDERA 3 FUNCIONES GENERALES:
        - CONSULTA DEL VALOR ACTUAL DE LOS INDICADORES DISPONIBLES, SEGUN LA WEB DE https://mindicador.cl/
        - CONSULTA EL VALOR DE LOS ULTIMOS 30 DIAS.
        - CONSULTA EL VALOR DE LOS INDICADORES PARA UNA FECHA EN ESPECIFICO. TAMBIEN LA FUNCION SE ENCUENTRA EN DISPONIBLE PARA CONSULTAR CON UN SOLO INDICADOR.
        - CONSULTA EL VALOR DE UN INDICADOR PARA UN AÑO EN ESPECIFICO.
        - LOS INDICADORES DISPONIBLES SON: ["uf", "ivp", "dolar", "dolar_intercambio", "euro", "ipc","utm", "imacec", "tpm", "libra_cobre", "tasa_desempleo", "bitcoin"]. PARA MAS DETALLE CONSULTAR mindicador.cl
        - TODAS LAS FUNCIONES RETORNAN UN OBJETO DE TIPO DICCIONARIO QUE PERMITE FACILMENTE TRABAJAR CON EL (ESTE SE PENSO PARA TRABAJAR CON PANDAS Y SEABORN)
    Returns:
        _type_: _description_
    """


# Listado con librerias necesarias
import requests
import json
import seaborn as sns
import pandas as pd
from datetime import datetime, timezone

import matplotlib.pyplot as plt
# %matplotlib inline


indicadores = ["uf", "ivp", "dolar", "dolar_intercambio", "euro", "ipc",
               "utm", "imacec", "tpm", "libra_cobre", "tasa_desempleo", "bitcoin"]

# POR PROGRAMAR:
# Convertirlo en una API que pueda llamar los metodos
# Crear tambien procesos y una API en SQL que me permita registrar mis compras personales en una base de datos.
# Buscar tambien una porcion de codigo que me permita borrar todos los temporales o archivos generados.

######################################################################################################
# FUNCION 1 DEL BOT: OBTIENE EL VALOR PARA EL DIA DE HOY DE LOS INDICADORES QUE PUEDE CONSULTAR LA API
######################################################################################################


def obtenerIndicadores():
    # Obtiene el valor actual de los indicadores [uf, ivp, dolar, dolar_intercambio, euro, ipc, utm, imacec, tpm, libra_cobre, tasa_desempleo, bitcoin]
    url = f'https://mindicador.cl/api/'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    return data


# Se genera una lista con indicadores para iterar (Es mucho mas rapido)
json_data = obtenerIndicadores()

# Muestra todos los indicadores rescatados de la consulta formateados de forma facil de leer
print("Los valores son mostrados a la fecha: " + json_data['fecha'][:10])

# Itera y muestra los indicadores
for indicador in indicadores:
    if (json_data[indicador]['nombre'] in ('Indice de Precios al Consumidor (IPC)', 'Imacec', 'Tasa de desempleo', 'Tasa Política Monetaria (TPM)')):
        print("El valor de " + json_data[indicador]['nombre'] + " corresponde a " +
              str((json_data[indicador]['valor'])) + " %")
    elif (json_data[indicador]['nombre'] in ('Unidad de fomento (UF)', 'Indice de valor promedio (IVP)', 'Dólar observado', 'Dólar acuerdo', 'Euro', 'Unidad Tributaria Mensual (UTM)')):
        print("El valor de " + json_data[indicador]['nombre'] + " corresponde a " +
              "$ "+str('{:,}'.format(json_data[indicador]['valor']).replace(',', '.')) + " " + json_data[indicador]['unidad_medida'])
    else:  # SON TODOS LOS INDICADORES CON VALOR EN DOLAR
        print("El valor de " + json_data[indicador]['nombre'] + " corresponde a " +
              "U$ "+str(json_data[indicador]['valor']) + " " + json_data[indicador]['unidad_medida'])
        if indicador == 'bitcoin':  # Se entrega el valor de BTC en PESOS
            print("El valor de " + json_data[indicador]['nombre'] + " corresponde a " +
                  "$ "+str('{:,}'.format(int(json_data[indicador]['valor']*json_data['dolar']['valor'])).replace(',', '.')) + " " + json_data['dolar']['unidad_medida'] + " App.")


#######################################################################################################

#######################################################################################################
# ----------------------------------SEGUNDA FUNCION DEL BOT
#######################################################################################################
# ENTREGA LA INFORMACION CORRESPONDIENTE A 30 DIAS HACIA ATRAS DADO UN INDICADOR ESPECIFICO.


def obtenerIndicador(indicador):  # RETORNA UN DICCIONARIO
    url = f'https://mindicador.cl/api/{indicador}'
    response = requests.get(url)
    data = json.loads(json.dumps(json.loads(
        response.text.encode("utf-8")), indent=2))
    # Para que el json se vea ordenado, retornar pretty_json
    # pretty_json = json.dumps(data, indent=2)
    return data


indicador = "uf"  # ESTE VALOR SE INGRESA DESDE EL TELEGRAM

# info_indicador = pd.DataFrame(data =obtenerIndicador("uf").items(), columns = [])
info_indicador = obtenerIndicador(indicador)

# Obtiene nombre del indicador consultado
nombre = info_indicador['nombre']  # el label a obtener es nombre
unidad_medida = info_indicador['unidad_medida']

# print(nombre)
# print(unidad_medida)

# Obtiene el valor diario con el timestamp de los ultimos 30 dias
serie = pd.DataFrame(info_indicador['serie'])
# Convierte la fecha en timestamp y añade las medidas necesarias para graficar.
serie['fecha'] = pd.to_datetime(serie["fecha"])
serie['dia'] = serie["fecha"].dt.day

# serie['mes'] = serie["fecha"].dt.month
# serie['año'] = serie["fecha"].dt.year


# IMPRIME EL DF CON LA FECHA EL PRIMER DIA
# print(serie)

# Generacion del grafico
# Proceso de formateo del grafico
sns.lineplot(serie, x=serie['dia'].sort_values(), y=serie['valor'])
# Añadir luego las fechas que se consideran
plt.suptitle("Valor en " + unidad_medida + " de Ult. 30 Dias " + nombre)
plt.ylabel("Valor en " + str(unidad_medida))
plt.xlabel("Dia del mes")
# Se muestra el grafico
plt.show()


# PUNTOS A CONSIDERAR PARA PROGRAMAR
# GRAFICAR LA MEDIA (O EL VALOR A LA MITAD DEL MES)
# RETORNAR LO ANTERIOR COMO MENSAJE POR MEDIO DE UN MENSAJE DEL BOT
# CONVERTIR EL OBJETO EN UNA IMAGEN PARA RETORNAR COMO MENSAJE


#######################################################################################################
# --------------------- AQUI TERMINA LA SEGUNDA FUNCION DEL BOT DE PYTHON -----------------------------
#######################################################################################################


#######################################################################################################
# --------------------- TERCERA FUNCION DEL BOT -----------------------------
#######################################################################################################

def obtenerIndicadorFecha(tipo_indicador, fecha):
    url = f'https://mindicador.cl/api/{tipo_indicador}/{fecha}'
    response = requests.get(url)
    data = json.loads(json.dumps(json.loads(
        response.text.encode("utf-8")), indent=2))
    # Para que el json se vea ordenado, retornar pretty_json
    # pretty_json = json.dumps(data, indent=2)
    return data


fecha = "17-12-2012"  # DEBE IR EN ESTE FORMATO
tipo_indicador = "bitcoin"


# Falta el print formateado de esta funcion
# print(obtenerIndicadorFecha(tipo_indicador, fecha))
# Falta añadir la fecha a la  funcion

if (obtenerIndicadorFecha(tipo_indicador, fecha)['nombre'] in ('Indice de Precios al Consumidor (IPC)', 'Imacec', 'Tasa de desempleo', 'Tasa Política Monetaria (TPM)')):
    print("El valor de " + obtenerIndicadorFecha(tipo_indicador, fecha)['nombre'] + " corresponde a " +
          str(obtenerIndicadorFecha(tipo_indicador, fecha)['serie'][0]['valor']) + " %")
elif obtenerIndicadorFecha(tipo_indicador, fecha)['nombre'] in ('Unidad de fomento (UF)', 'Indice de valor promedio (IVP)', 'Dólar observado', 'Dólar acuerdo', 'Euro', 'Unidad Tributaria Mensual (UTM)'):
    print("El valor de " + obtenerIndicadorFecha(tipo_indicador, fecha)['nombre'] + " corresponde a " +
          "$ "+str('{:,}'.format(obtenerIndicadorFecha(tipo_indicador, fecha)['serie'][0]['valor']).replace(',', '.')) + " " + obtenerIndicadorFecha(tipo_indicador, fecha)['unidad_medida'])
else:  # SON TODOS LOS INDICADORES CON VALOR EN DOLAR
    # Si el atributo serie viene vacio, entonces sale del a funcion en caso contrario lo imprime.
    if obtenerIndicadorFecha(tipo_indicador, fecha)['nombre'] == 'Bitcoin' and not obtenerIndicadorFecha(tipo_indicador, fecha)['serie']:
        print("El valor de " + obtenerIndicadorFecha(tipo_indicador, fecha)
              ['nombre'] + " no tiene registro para la fecha consultada")
    else:
        print("El valor de " + obtenerIndicadorFecha(tipo_indicador, fecha)['nombre'] + " corresponde a " +
              "U$ "+str(obtenerIndicadorFecha(tipo_indicador, fecha)['serie'][0]['valor']) + " " + obtenerIndicadorFecha(tipo_indicador, fecha)['unidad_medida'])

# # LA MISMA FUNCION PERO ITERABLE

print("La fecha consultada para el valor de los indicadores es: " + fecha)

for label in indicadores:
    if (obtenerIndicadorFecha(label, fecha)['nombre'] in ('Indice de Precios al Consumidor (IPC)', 'Imacec', 'Tasa de desempleo', 'Tasa Política Monetaria (TPM)')):
        print("El valor de " + obtenerIndicadorFecha(label, fecha)['nombre'] + " corresponde a " +
              str(obtenerIndicadorFecha(label, fecha)['serie'][0]['valor']) + " %")
    elif obtenerIndicadorFecha(label, fecha)['nombre'] in ('Unidad de fomento (UF)', 'Indice de valor promedio (IVP)', 'Dólar observado', 'Dólar acuerdo', 'Euro', 'Unidad Tributaria Mensual (UTM)'):
        print("El valor de " + obtenerIndicadorFecha(label, fecha)['nombre'] + " corresponde a " +
              "$ "+str('{:,}'.format(obtenerIndicadorFecha(label, fecha)['serie'][0]['valor']).replace(',', '.')) + " " + obtenerIndicadorFecha(label, fecha)['unidad_medida'])
    else:  # SON TODOS LOS INDICADORES CON VALOR EN DOLAR
        # Si el atributo serie viene vacio, entonces sale del a funcion en caso contrario lo imprime.
        if obtenerIndicadorFecha(label, fecha)['nombre'] == 'Bitcoin' and not obtenerIndicadorFecha(label, fecha)['serie']:
            break
        else:
            print("El valor de " + obtenerIndicadorFecha(label, fecha)['nombre'] + " corresponde a " +
                  "U$ "+str(obtenerIndicadorFecha(label, fecha)['serie'][0]['valor']) + " " + obtenerIndicadorFecha(label, fecha)['unidad_medida'])

# # COSAS PENDIENTES
# # EL INGRESO DE LA VARIABLE DEBE VENIR DESDE EL MENSAJE DEL TELEGRAM (HACER TAMBIEN LA VERSION DE INGRESO POR CONSOLA DE PYTHON)

#######################################################################################################
# # ---------------------------- HASTA AQUI LA TERCERA FUNCION DEL BOT -----------------------------
#######################################################################################################

#######################################################################################################
# ------------------------------------- CUARTA FUNCION DEL BOT  ---------------------------------------
#######################################################################################################

tipo_indicador = "uf"
anio = '1989'

# Obtiene los valores del indicador un año determinado.

# Considerar tambien las validaciones de los activos que no tienen valor un año determinado


def obtenerIndicadorAño(tipo_indicador, anio):
    url = f'https://mindicador.cl/api/{tipo_indicador}/{anio}'
    response = requests.get(url)
    data = json.loads(json.dumps(json.loads(
        response.text.encode("utf-8")), indent=2))
    # Para que el json se vea ordenado, retornar pretty_json
    # pretty_json = json.dumps(data, indent=2)
    return data


# Obtiene la informacion del indicador
info_indicador = obtenerIndicadorAño(tipo_indicador, anio)

# Guarda el nombre y la unidad de medida del indicador
nombre = info_indicador['nombre']
unidad_medida = info_indicador['unidad_medida']

# print(nombre)
# print(unidad_medida)

# Obtiene el valor diario con el timestamp de los ultimos 30 dias
serie = pd.DataFrame(info_indicador['serie'])
# Convierte la fecha en timestamp y añade las medidas necesarias para graficar.
serie['fecha'] = pd.to_datetime(serie["fecha"])
# Se ordena el DF
serie = serie.sort_values('fecha')

# IMPRIME EL DF CON LA FECHA EL PRIMER DIA
# print(serie.sort_values('fecha'))

# Generacion del grafico
sns.lineplot(serie, x=serie['fecha'], y=serie['valor'])
# Formato de la visualizacion
plt.suptitle("Valor en " + unidad_medida + " del Ult. año de " + nombre)
plt.ylabel("Valor en " + str(unidad_medida))
plt.xlabel("Año mes")

# # Se muestra el grafico
plt.show()

# Cosas que faltan formatear
# Retornar la foto en el mensaje que vuelve hacia el telegram.
