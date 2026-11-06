import json

class GestorInventario:
    @staticmethod    
    def guardar_catalogo_json(lista_dispositivos: list, ruta: str)->None:
            datos_serializables = [dispositivo.__dict__ for dispositivo in lista_dispositivos]
            with open (ruta, "w", encoding= "utf-8") as archivo:
                json.dump(datos_serializables, archivo, indent=4, ensure_ascii=False)