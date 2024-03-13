import json
plantilla = '[{"nombre": "miguel"},{"nombre" : "john"},["hola mundo"]]'
plantilla = json.loads(plantilla)

example = list(
    dict(["nombre": "miguel"]),
    dict(["nombre" : "john"]),
    list(["hola mundo"])
)
json.dumps(example, indent=4)