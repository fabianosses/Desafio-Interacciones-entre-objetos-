
from producto import Producto
from abc import ABC, abstractmethod

# Clase principal Tienda
class Tienda(ABC):
  def __init__(self, nombre, delivery):
    self._nombre = nombre
    self._delivery = delivery
    self.productos = []

  @abstractmethod
  def ingresar_producto(self, nombre, precio, stock = 0):
    pass

  @abstractmethod
  def listar_productos(self):
    pass

  @abstractmethod
  def vender_producto(self, nombre_producto, cantidad):
    pass

  def get_nombre(self):
      return self._nombre

  def get_delivery(self):
      return self._delivery
  
# Subclase Restaurante -->hereda<-- de la principal Tienda
class Restaurante(Tienda):
  def __init__(self, nombre, delivery):
    super().__init__(nombre, delivery)
    print(f"nombre restaurante: {nombre} valor delivery: {delivery}")
  def ingresar_producto(self, nombre, precio, stock = 0):
    nuevo_producto = Producto(nombre, precio, stock)  # Stock siempre es 0 en Restaurante
    print(nuevo_producto)
    for producto in self.productos:
       if producto == nuevo_producto:
          producto + nuevo_producto
          return
    self.productos.append(nuevo_producto)
  def listar_productos(self):
    result = f"Productos en {self._nombre}:\n"
    for producto in self.productos:
        result += f"- {producto.get_nombre()}, Precio: {producto.get_precio()}\n"  # Oculta el stock
    return result
  def vender_producto(self, nombre_producto, cantidad):
        # No es necesario validar stock en Restaurante
        producto_encontrado = False
        for producto in self.productos:
          if producto.get_nombre() == nombre_producto:
            producto_encontrado = True
            break
        if not producto_encontrado:
          print(f"Producto {nombre_producto} no encontrado en {self._nombre}.")
        else:
          print(f"Venta de {cantidad} {nombre_producto}(s) realizada en {self._nombre}.")

# Subclase Supermercado que -->hereda<-- de la principal
class Supermercado(Tienda):
  def __init__(self, nombre, delivery):
       super().__init__(nombre, delivery)
  def ingresar_producto(self, nombre, precio, stock=0):
      nuevo_producto = Producto(nombre, precio, stock)
      for producto in self.productos:
        if producto == nuevo_producto:
          producto + nuevo_producto
          return
      self.productos.append(nuevo_producto)
  def listar_productos(self):
    result = f"Productos en {self._nombre}:\n"
    for producto in self.productos:
        stock_info = f", Stock: {producto.get_stock()}"
        if producto.get_stock() < 10:
          stock_info += " (Pocos productos disponibles)"
        result += f"- {producto.get_nombre()}, Precio: {producto.get_precio()}{stock_info}\n"
    return result
  def vender_producto(self, nombre_producto, cantidad):
    for producto in self.productos:
      if producto.get_nombre() == nombre_producto:
          if producto.get_stock() == 0:
            print(f"No hay stock disponible de {nombre_producto} en {self._nombre}.")
            return
          if producto.get_stock() < cantidad:
              cantidad_vendida = producto.get_stock()
              producto.set_stock(0)
              print(f"Solo se vendieron {cantidad_vendida} {nombre_producto}(s) debido al stock limitado en {self._nombre}.")
          else:
              producto - cantidad
              print(f"Venta de {cantidad} {nombre_producto}(s) realizada en {self._nombre}.")
          return
    print(f"Producto '{nombre_producto}' no encontrado en {self._nombre}.")

# Subclase Farmacia que -->hereda<-- de la principal
class Farmacia(Tienda):
  def __init__(self, nombre, delivery):
      super().__init__(nombre, delivery)
      print(f"nombre farmacia: {nombre} valor delivery: {delivery}")
  def ingresar_producto(self, nombre, precio, stock=0):
      nuevo_producto = Producto(nombre, precio, stock)
      for producto in self.productos:
        if producto == nuevo_producto:
          producto + nuevo_producto
          return
      self.productos.append(nuevo_producto)
  def listar_productos(self):
      result = f"Productos en {self._nombre}:\n"
      for producto in self.productos:
          precio_info = f"Precio: {producto.get_precio()}"
          if producto.get_precio() > 15000:
              precio_info += " (Envío gratis al solicitar este producto)"
          result += f"- {producto.get_nombre()}, {precio_info}\n"  # Oculta el stock
      return result
  def vender_producto(self, nombre_producto, cantidad):
    if cantidad > 3:
        print("No se puede solicitar una cantidad superior a 3 por producto en Farmacia.")
        return
    for producto in self.productos:
        print(self.productos)
        if producto.get_nombre() == nombre_producto:
            if producto.get_stock() == 0:
              print(f"No hay stock disponible de {nombre_producto} en {self._nombre}.")
              return
            if producto.get_stock() < cantidad:
                cantidad_vendida = producto.get_stock()
                producto.set_stock(0)
                print(f"Solo se vendieron {cantidad_vendida} {nombre_producto}(s) debido al stock limitado en {self._nombre}.")
            else:
                producto - cantidad
                print(f"Venta de {cantidad} {nombre_producto}(s) realizada en {self._nombre}.")
            return
    print(f"Producto '{nombre_producto}' no encontrado en {self._nombre}.")