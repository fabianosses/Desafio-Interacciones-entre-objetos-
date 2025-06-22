class Producto:
    def __init__(self, nombre: str, precio: int, stock: int = 0):
        self.__nombre = nombre
        self.__precio = precio
        self. stock = stock

    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()

    def __add__(self, agregar_producto):
        if self.__nombre == agregar_producto.__nombre:
            nuevo_stock = self.stock + agregar_producto.stock
            return Producto(nombre=self.__nombre, precio=self.__precio, stock=nuevo_stock)
        else:
            return [self, agregar_producto]
        