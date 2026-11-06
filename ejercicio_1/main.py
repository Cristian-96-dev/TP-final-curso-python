import funciones 

registros_crudos = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": " SENSOR-002", "temperatura": "30.1 C", "ubicacion": "Planta Sur"},
    {"sensor_id": "SENSOR-003 ", "temperatura": "22.0"} 
]

lista_limpia = []
for registro in registros_crudos:
    diccionario_estandarizado = funciones.limpiar_registro_lector(registro)
    lista_limpia.append(diccionario_estandarizado)


sensores_alerta, promedio = funciones.generar_resumen_sensores(lista_limpia, 25.0)
print("---DICCIONARIO ESTANDARIZADO---")
print(diccionario_estandarizado)
print("--- REPORTE TÉRMICO DE PLANTA ---")
print(f"Promedio térmico global: {promedio:.2f}°")
print(f"Dispositivos en estado de alerta: {sensores_alerta}")



