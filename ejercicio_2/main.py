import json

class DispositivoTecnologico:
    stock: int
    precio: float
    ficha_tecnica: str


    def __init__(self, stock: int, precio: float):
        self.stock = stock
        self.precio = precio
        self.ficha_tecnica = "El producto no tiene asignado una ficha técnica."

    def obtener_ficha_tecnica(self):
        return self.ficha_tecnica

    def stock_positivo(self):
        if self.stock < 0:
            raise StockInvalidoError("El stock no debe tomar valores negativos.")

class Panelsolar(DispositivoTecnologico):
    def __init__(self, stock: int, precio: float, detalle_tecnico: str):
        super().__init__(stock, precio)
        self.detalle_tecnico = detalle_tecnico

    def obtener_ficha_tecnica(self):
        return f"Ficha técnica. Panel Solar: {self.detalle_tecnico}"

    def __str__(self):
        return f"Panel Solar (Stock: {self.stock}, Precio: {self.precio})"
    
class StockInvalidoError(Exception):pass

class GestorInventario:
    @staticmethod    
    def guardar_catalogo_json(lista_dispositivos: list, ruta: str)->None:
            datos_serializables = [dispositivo.__dict__ for dispositivo in lista_dispositivos]
            with open (ruta, "w", encoding= "utf-8") as archivo:
                json.dump(datos_serializables, archivo, indent=4, ensure_ascii=False)

termo_tanque = DispositivoTecnologico(35, 500000)
panel_fotovoltaico = Panelsolar(20, 350000, "80000 W/h")
panel_termico = Panelsolar(-20, 325000, "75000 W/h")
panel_mixto = Panelsolar(20, 400000, "100000 W/h")

persistencia_json = "catalogo_ecotech.json"
GestorInventario.guardar_catalogo_json([panel_fotovoltaico, panel_mixto, termo_tanque], persistencia_json) 
print(panel_fotovoltaico.obtener_ficha_tecnica())
print(panel_termico)
print(panel_mixto)
print(f"Ficha tecnica del termo-tanque: {termo_tanque.obtener_ficha_tecnica()}")
print(panel_termico.stock_positivo())
