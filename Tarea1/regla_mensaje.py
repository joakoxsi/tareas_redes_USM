from datetime import datetime 
import re
import json


def mensaje_inicials():
    largo=str(input("Ingrese el largo min del mensaje: "))
    palabra=str(input("Ingrese la palabra inicial del mensaje: "))
    time=datetime.now()#hago el registo del tiempo
    mensaje=f"{time}-{largo}-{1}-{palabra}" #concateno todo para obtener el mensaje final 
    return mensaje




def crear_mensaje(mensaje_recido):
    palabra=str(input("Ingrese la palabra adicional: "))
    mensaje_recido= re.split(r"-", mensaje_recido) # separo el mensaje en base a los - que hay 
    texto=f"{mensaje_recido[5]} {palabra}" # tomo el texto anterior le añado un espacio y luego pongo la nueva palabra
    largo_actual= int(mensaje_recido[4])+1 #actualizo las palabras actuales
    time=datetime.now()#hago el registo del tiempo
    mensaje_nuevo=f"{time}-{mensaje_recido[3]}-{largo_actual}-{texto}" #concateno todo para obtener el mensaje final 
    print(mensaje_nuevo)
    return mensaje_nuevo 



def crear_Json(mensaje_actual):
    time=datetime.now()#hago el registo del tiempo
    mensaje_recido= re.split(r"-", mensaje_actual)
    datos={
        "timestamp": str(time),
        "largo_minimo": mensaje_recido[3],
        "largo_actual": mensaje_recido[4],
        "mensaje": mensaje_recido[5]

    }
    mensaje_json=json.dumps(datos)
    print(mensaje_json)
    return mensaje_json
    



