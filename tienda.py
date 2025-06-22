
from producto import Producto
from abc import ABC, abstractmethod

# Clase principal Tienda
class Tienda(ABC):
  def __init__(self, nombre, delivery):
    self.__nombre = nombre
    self.__delivery = delivery
    self.productos = []

  @abstractmethod
  def ingresar_producto(self, producto):
    pass

  @abstractmethod
  def listar_productos(self):
    pass

  @abstractmethod
  def vender_producto(self, producto):
    pass

# Subclase que -->hereda<-- de la principal
class Restaurante(Tienda):
  def __init__(self, nombre: str, delivery):
       super().__init__(nombre, delivery)
       print(f"nombre restaurante: {nombre} valor delivery: {delivery}")

  def ingresar_producto(self, producto: Producto):
    for p in self.productos:
        if p == producto:
            p += producto
            return
    self.productos.append(producto)

  def listar_productos(self):
    for producto in self.productos:
      print(producto)

  def vender_producto(self, producto: Producto):
    if producto in self.productos:
      self.productos.remove(producto)
      return producto
    else:
      return None

# Subclase que -->hereda<-- de la principal
class Supermercado(Tienda):
  def __init__(self, nombre: str, delivery):
       super().__init__(nombre, delivery)
       print(f"nombre Supermercado: {nombre} valor delivery: {delivery}")

  def ingresar_producto(self, producto: Producto):
    for p in self.productos:
        if p == producto:
            p += producto
            return
    self.productos.append(producto)

  def listar_productos(self):
    for producto in self.productos:
      print(producto)

  def vender_producto(self, producto: Producto):
    if producto in self.productos:
      self.productos.remove(producto)
      return producto
    else:
      return None

# Subclase que -->hereda<-- de la principal
class Farmacia(Tienda):
  def __init__(self, nombre: str, delivery):
       super().__init__(nombre, delivery)
       print(f"nombre farmacia: {nombre} valor delivery: {delivery}")

  def ingresar_producto(self, producto: Producto):
    for p in self.productos:
        if p == producto:
            p += producto
            return
    self.productos.append(producto)

  def listar_productos(self, stock_minimo=None):
    if stock_minimo is None:
        for producto in self.productos:
            print(producto)
    else:
        for producto in self.productos:
            if producto.stock < stock_minimo:
                print(producto)

  def vender_producto(self, producto: Producto):
    for i, p in enumerate(self.productos):
        if p == producto:
            if p.stock > 0:
                p.stock -= 1
                return p
            else:
                return None
    return None