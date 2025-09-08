import json

# Supongamos que recibes una respuesta en texto JSON
respuesta = '{"nombre": "Benja", "edad": 21}'
data = json.loads(respuesta)  # lo convierte en diccionario

print(data["nombre"])  # "Benja"
print(data["edad"])    # 21

respuesta = '[{"nombre":"Benja","edad":21},{"nombre":"Ana","edad":20}]'
data = json.loads(respuesta)  # lista de diccionarios

for persona in data:
    print(persona["nombre"], persona["edad"])