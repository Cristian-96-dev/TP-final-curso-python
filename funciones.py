import re
import statistics

def limpiar_registro_lector(regitro_raw: dict)-> dict:
    """Rcibe un dict con datos que pueden venir sucios o incompletos, y devuelve un dict estadarizado y limpio."""
    sensor_id = regitro_raw.get("sensor_id", "").strip()

    temperatura_raw = str(regitro_raw.get("temperatura", ""))
    extraccion = re.search(r'\d+\.?\d*', temperatura_raw)
    temperatura = float(extraccion.group()) if extraccion else 0.0

    ubicacion = regitro_raw.get("ubicacion", "desconocida")

    return {
            "sensor_id": sensor_id,
            "temperatura": temperatura,
            "ubicacion": ubicacion
        }

def generar_resumen_sensores(lista_sensores_limpios: dict, umbral_temperatura: float)->tuple:
    """Recibe un dict previamente estandarizado de datos de sensores y un umbral de temperatura. Y devuelve una lista de los sensores que han superado el umbral y un promedio global de la temperatura."""
    lista_sensores_alerta = []
    temperaturas = []

    for sensor in lista_sensores_limpios:
        temp = sensor.get("temperatura")
        temperaturas.append(temp)

        if temp > umbral_temperatura:
            lista_sensores_alerta.append(sensor.get("sensor_id"))

    promedio_temperatura = statistics.mean(temperaturas) if temperaturas else 0.0

    return (lista_sensores_alerta, promedio_temperatura)