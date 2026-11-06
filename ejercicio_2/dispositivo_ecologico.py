from stock_invalido import StockInvalidoError

class DispositivoEcologico:
    def __init__(self, stock: int, precio: float):
        self.stock = stock  
        self.precio = precio
        self.ficha_tecnica = "El producto no tiene asignado una ficha técnica."

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError("El stock no debe tomar valores negativos.")
        self._stock = valor

    def obtener_ficha_tecnica(self):
        return self.ficha_tecnica

class PanelSolar(DispositivoEcologico):
    def __init__(self, stock: int, precio: float, detalle_tecnico: str):
        super().__init__(stock, precio)
        self.detalle_tecnico = detalle_tecnico

    def obtener_ficha_tecnica(self):
        return f"Ficha técnica. Panel Solar: {self.detalle_tecnico}"

    def __str__(self):
        return f"Panel Solar (Stock: {self.stock}, Precio: {self.precio})"