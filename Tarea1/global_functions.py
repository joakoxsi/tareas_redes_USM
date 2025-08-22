from datetime import datetime 
import re
import json


def contar_palabras(msg: str) -> int:
    """Cuenta palabras del mensaje (se usa como LargoActual)."""
    return len([w for w in msg.strip().split() if w])

def componer_string(minimo: int, mensaje: str, ts: str | None = None) -> str:
    """Arma el string con el formato [Timestamp]-[LargoMinimo]-[LargoActual]-[Mensaje]."""
    if ts is None:
        ts = datetime.now().isoformat(sep=" ", timespec="seconds")
    largo_actual = contar_palabras(mensaje)
    return f"{ts}-{minimo}-{largo_actual}-{mensaje}"

def parsear_string(mensaje_formateado: str):
    """
    Intenta parsear el formato:
       [Timestamp]-[LargoMinimo]-[LargoActual]-[Mensaje]
    Devuelve dict con claves: timestamp, min_len, cur_len, msg  (o None si no calza).
    Acepta timestamps entre [] o sin [] para robustez.
    """
    mensaje_formateado = mensaje_formateado.strip()
    m = re.match(r'^\[?(.+?)\]?-(\d+)-(\d+)-(.+)$', mensaje_formateado)
    if not m:
        return None
    ts, min_len, cur_len, msg = m.groups()
    return {
        "timestamp": ts.strip(),
        "min_len": int(min_len),
        "cur_len": int(cur_len),
        "msg": msg.strip(),
    }


def mensaje_inicials():
    while True:
        largo = input("Ingrese el largo min del mensaje: ")
        try:
            # Intentamos convertir el input a entero
            largo = int(largo)
            break  # Si no ocurre un error, el valor es válido
        except:
            print("Por favor, ingrese un número entero.")
            
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
