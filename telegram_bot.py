"""
    ESTE SCRIPT ES UNA IMPLEMENTACION SIMPLE DE LA API ALOJADA EN https://mindicador.cl/

    LA IMPLEMENTACION ACTUAL CONSISTE EN CONSULTAS SIMPLES QUE SERAN EJECUTADAS POR UN BOT DE TELEGRAM, EL BACK ESTA CONSTRUIDO SOBRE UN MISMO SCRIPT CON FUNCIONES EN PYTHON ALOJADAS EN ESTE MISMO REPO
    -- EN DESARROLLO --
    LA IMPLEMENTACION CONSIDERA 4 FUNCIONES GENERALES:
        - CONSULTA DEL VALOR ACTUAL DE LOS TODOS LOS INDICADORES DISPONIBLES, SEGUN LA WEB DE https://mindicador.cl/
        - CONSULTA EL VALOR DE LOS ULTIMOS 30 DIAS, DE UN ACTIVO DETERMINADO. RETORNA UNA IMAGEN CON UN GRAFICO DEL INDICADOR.
        - CONSULTA EL VALOR DE LOS INDICADORES PARA UNA FECHA EN ESPECIFICO. TAMBIEN LA FUNCION SE ENCUENTRA EN DISPONIBLE PARA CONSULTAR CON UN SOLO INDICADOR, EN UNA FECHA EN ESPECIFICO.
        - CONSULTA EL VALOR DE UN INDICADOR PARA UN AÑO EN ESPECIFICO. RETORNA UNA IMAGEN CON EL GRAFICO DEL COMPORTAMIENTO PARA ESE AÑO.
        - LOS INDICADORES DISPONIBLES SON: ["uf", "ivp", "dolar", "dolar_intercambio", "euro", "ipc","utm", "imacec", "tpm", "libra_cobre", "tasa_desempleo", "bitcoin"]. PARA MAS DETALLE CONSULTAR mindicador.cl
        - TODAS LAS FUNCIONES RETORNAN UN OBJETO DE TIPO DICCIONARIO QUE PERMITE FACILMENTE TRABAJAR CON EL (ESTE SE PENSO PARA TRABAJAR CON PANDAS Y SEABORN)
    Returns:
        _type_: _description_
"""

# RECUERDA QUE ESTE BOT TIENE SUS DEPENDENCIAS INSTALADAS EN EL VENV DE DATANALYSIS

import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater
from dotenv import load_dotenv, dotenv_values
from datetime import datetime
from app import indicadoresDiarios, obtenerIndicadoresXFecha, ultimoMesIndicador, obtenerIndicadorXAño

config = load_dotenv(
    r'D:\Users\JuanIgnacio\Cursos_Online\Study Devs\01-Indicadores_chilenos\variables.env')
# config = load_dotenv(find_dotenv()) # ASEGURATE QUE EL ARCHIVO CON LAS
config = dotenv_values('examples.env')

# SE CARGAN VARIABLES DE ENTORNO
TOKEN = os.getenv('TOKEN')  # LOGIN TOKEN
BOT_USERNAME: Final = os.getenv('BOTUSERNAME')  # NOMBRE DEL BOT

# Aqui se programan los comandos que se desplegan en el menu
# Consulta

# Este es el texto que recibe cuando comienzas a interactuar con el bot


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''Hola! Soy Fintualbot, un asistente que te entrega las estadisticas mas importantes sonbre los indicadores macroeconomicos de chile (estos corresponden a: uf, ivp, dolar, dolar_intercambio, euro, ipc,utm, imacec, tpm, libra_cobre, tasa_desempleo, bitcoin).\n
    La API se basa en una implementacion simplificada y user friendly de miindicador.cl.\n
    Su uso simplemente se basa en las funciones listadas a continuacion, para hacer uso de ellas, solo debes seleccionar el numero y seguir las instrucciones:
    (1) Consulta el valor al día de hoy de los activos/indicadores mas importantes de la economia chilena. \n *(OK)*
    (2) Consulta el valor de un indicador durante los ultimos 30 dias y entrega un grafico con el comportamiento.\n 
    (3) Consulta el valor de los indicadores para una fecha en especfico. (posterior a 1980, excepto bitcoin). \n 
    (4) Consulta el valor de un año de un indicador especifico. Retorna un grafico mostrando su comportamiento.\n 
    ''')
# Si quieres aportar con el desarrollo de la plataforma puedes donar a continuación: DIRECCION BTC


# Este es el texto que recibe cuando comienzas a interactuar con el bot


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''Aqui encontraras mas informacion sobre cada una de las 4 funciones programadas para el bot y sus parametros.
                                    (1) Consulta el valor diario de los activos/indicadores disponibles en la API. ( uf, ivp, dolar, dolar_intercambio, euro, ipc,utm, imacec, tpm, libra_cobre, tasa_desempleo, bitcoin) \n
                                    (2) Consulta el valor de un indicador durante los ultimos 30 dias o ultimo mes y entrega un grafico con el resultado. Considera como parametro la abreviatura del indicador\n (En desarrollo)
                                    (3) Consulta (uno/varios indicadores para un mismo valor de fecha) (posterior a 1980, excepto bitcoin).Considera como parametro la fecha y/o el indicador . \n (En desarrollo)
                                    (4) Consulta el valor de un año de un indicador especifico. Retorna un grafico mostrando su comportamiento.Considera como parametro la fecha y\n (En desarrollo)
                                    ''')

# Estes es el texto que recibe cuando comienzas a interactuar con el bot


async def obtener_indicadores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(indicadoresDiarios())


async def valorXFecha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fecha = str(context.args[0])
    if datetime.date(datetime.strptime(fecha, "%d-%m-%Y")):
        await update.message.reply_text(obtenerIndicadoresXFecha(str(fecha)))
    # await update.message.reply_text('La fecha ingresada no es valida u ocurrio otro error.')


async def Ult30DIndicador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    indicador = str(context.args[0])  # obtiene el indicador
    file = ultimoMesIndicador(indicador)
    with open(file, 'rb') as photo:
        await context.bot.send_photo(chat_id=update.message.chat.id, photo=photo)

    # Eliminar el archivo después de enviarlo
    if os.path.exists(file):
        os.remove(file)


async def UltimoAnoIndicador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ano = str(context.args[0])  # obtiene año
    indicador = str(context.args[1])  # otiene año
    file = obtenerIndicadorXAño(ano, indicador)
    with open(file, 'rb') as photo:
        await context.bot.send_photo(chat_id=update.message.chat.id, photo=photo)

    # Eliminar el archivo después de enviarlo
    if os.path.exists(file):
        os.remove(file)


# Responses
# Aqui maneja las respuestas cuanto se recibe un mensaje
# Aqui tengo que hacer o mandar a llamar las ejecuciones del bot


def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hola' in processed:
        return 'Hola Bienvenido!'
    if ('como estas?' or 'cómo estás?') in processed:
        return 'Estoy bien!'
    if 'donde estoy?' in processed:
        return 'Soy un boot que te permite obtener la principal informacion financiera de Chile!'

    ######################################################################################
    #### DE AQUI EN ADELANTE VOY A IR PROBANDO Y PROGRAMANDO DIFERENTES FUNCIONES ########
    ######################################################################################
    if '1' in processed:
        # Devuelve un String con la informacion de los indicadores diarios al ultimo dia habil.
        return indicadoresDiarios()
    if '2' in processed:
        return 'Para obtener el gráfico de los indicadores en la fecha deseada escribe lo siguiente /command4 "Simbolo" (Con el valor del indicador).'
    if '3' in processed:
        return 'Para obtener el valor de los indicadores en la fecha deseada escribe lo siguiente /command5 "DD-MM-YYYY" (Con el valor del dia a consultar).'
    if '4' in processed:
        return 'Para obtener el gráfico de los indicadores en la fecha deseada escribe lo siguiente /command6 "YYYY" "Simbolo" (Con el valor del año e indicador).'

    ######################################################################################
    #### DE AQUI EN ADELANTE VOY A IR PROBANDO Y PROGRAMANDO DIFERENTES FUNCIONES ########
    ######################################################################################

    return '''Elige alguna de las siguientes opciones para ejecutar:
    (1) Valor de los activos chilenos hoy.
    (2) Valor de un indicador los ultimos 30 dias.
    (3) Valor de los indicador(es) para una fecha en especifico (posterior a 1980, excepto bitcoin) 
    (4) Valor del ultimo año de un indicador. 
    Puedes consultar mas sobre las funciones en los comandos disponibles en el menú
    '''


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Considera si el tipo de mensaje es un chat privado o un grupo.
    message_type: str = update.message.chat.type
    text: str = update.message.text  # este es el mensaje que vamos a procesar.

    # Va a mostrar el mensaje en que tipo de interacion lo hace (privado o en grupo)
    print(f'User ({update.message.chat.id} in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            # Se quita el valor del usuario en lo recibido por consola
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # No responde nada
    else:
        response: str = handle_response(text)  # Entrega una respuesta

        print('Bot', response)  # Debug
        await update.message.reply_text(response)


# Funcion que maneja los errores
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    await update.message.reply_text('Ocurrio un error con la solicitud generada, intentalo nuevamente o utiliza otra funcion.')


if __name__ == '__main__':
    print('El Bot se esta iniciando...')
    app = Application.builder().token(TOKEN).build()

    # COMMANDS
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('command3', obtener_indicadores))
    # Para añadir un nuevo comando a las respuestas del bot
    app.add_handler(CommandHandler('command4', valorXFecha))
    app.add_handler(CommandHandler('command5', Ult30DIndicador))
    app.add_handler(CommandHandler('command6', UltimoAnoIndicador))

    # MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # ERRORS
    app.add_error_handler(error)

    # POLLS THE BOT
    print('Cargando la API...')
    app.run_polling(poll_interval=3)  # En segundos.
