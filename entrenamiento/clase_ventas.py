"""
Aquí se encuentra la clase para la tienda de indumentaria, se puede modificar a gusto del programador
"""

class Ticket:
    def __init__(self,fecha,id_pedido, cliente,sku,talle,color,cantidad,precio,estado):
        self.fecha = fecha
        self.id = id_pedido
        self.cliente = cliente
        self.sku = sku
        self.talle = talle
        self.color = color
        self.cant = cantidad
        self.precio = precio
        self.estado = estado

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        cadena = (str(self.fecha) + ";" + str(self.id) + ";" + str(self.cliente) +
                  ";" + str(self.sku) + ";" + str(self.talle) + ";" + str(self.color) +
                  ";" + str(self.cant) + ";" + str(self.precio) + ";" + str(self.estado))
        return cadena