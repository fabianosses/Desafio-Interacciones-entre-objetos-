class Producto:
    def __init__(self, nombre, precio, stock = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.stock = max(0, stock)  # Asegura que el stock no sea negativo

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.__nombre == other.__nombre

    def __add__(self, other):
        if isinstance(other, Producto) and self.__nombre == other.__nombre:
            self.stock += other.stock
            return self

    def __sub__(self, cantidad):
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad a restar debe ser un entero positivo.")
        self.stock = max(0, self.stock - cantidad)
        return self
        
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = max(0, stock)  # Asegura que el stock no sea negativo

    def __str__(self):
        return f"Nombre: {self.__nombre}, Precio: {self.__precio}, Stock: {self.stock}"