from dispositivo_ecologico import PanelSolar
from stock_invalido import StockInvalidoError
from gestor_inventario import GestorInventario

catalogo_valido = []

try:
    mixto = PanelSolar(30, 300000, "85000 W/h")
    fotovoltaico = PanelSolar(20, 350000.0, "80000 W/h")
    catalogo_valido.append(fotovoltaico)
    catalogo_valido.append(mixto)
    print("Productos instanciados con éxito.")

    termico = PanelSolar(-20, 325000.0, "75000 W/h")
    catalogo_valido.append(termico)

except StockInvalidoError as error:
    print(f"Se bloqueó un ingreso al inventario: {error}")
    
finally:
    ruta_archivo = "catalogo_ecotech.json"
    GestorInventario.guardar_catalogo_json(catalogo_valido, ruta_archivo)
    print(f"Proceso finalizado. Se exportaron {len(catalogo_valido)} producto(s) al archivo {ruta_archivo}.")
