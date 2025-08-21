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