from datetime import datetime

FORMATO = "%Y-%m-%d %H:%M:%S"


def registrar_respuesta(usuario):
    fecha = datetime.now().strftime(FORMATO)

    with open("respuesta.log", "a", encoding="utf-8") as archivo:
        archivo.write(f"{fecha},USUARIO_BLOQUEADO,{usuario}\n")

    return fecha


intentos = {}

with open("eventos.log", "r", encoding="utf-8") as archivo:

    for linea in archivo:

        linea = linea.strip()
        if not linea:
            continue

        fecha, tipo, usuario = linea.split(",")

        if tipo == "LOGIN_FALLIDO":

            if usuario not in intentos:
                intentos[usuario] = []

            intentos[usuario].append(fecha)

lista_mttd = []
lista_mttr = []

for usuario, registros in intentos.items():

    if len(registros) >= 3:

        print("ALERTA DE SEGURIDAD")
        print("Usuario:", usuario)
        print("Intentos fallidos:", len(registros))
        print("Primer intento:", registros[0])
        print("Detección:", registros[2])

        fecha_respuesta = registrar_respuesta(usuario)

        print("Acción aplicada: bloqueo de usuario")
        print("Respuesta:", fecha_respuesta)

        inicio = datetime.strptime(registros[0], FORMATO)
        deteccion = datetime.strptime(registros[2], FORMATO)
        respuesta = datetime.strptime(fecha_respuesta, FORMATO)

        mttd = (deteccion - inicio).total_seconds()
        print("MTTD:", mttd, "segundos")

        mttr = (respuesta - deteccion).total_seconds()
        print("MTTR:", mttr, "segundos")

        lista_mttd.append(mttd)
        lista_mttr.append(mttr)

        print("-" * 40)

if lista_mttd:
    print("MTTD promedio:", sum(lista_mttd) / len(lista_mttd), "segundos")
    print("MTTR promedio:", sum(lista_mttr) / len(lista_mttr), "segundos")
else:
    print("No se detectaron incidentes.")
