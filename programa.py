from tienda import Restaurante, Supermercado, Farmacia

def crear_tienda():
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): ")
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = int(input("Ingrese el costo de delivery: "))
    if tipo_tienda.lower() == "restaurante":
        return Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        return Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        return Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return None

def ingresar_productos(tienda):
    while True:
        continuar = input("¿Desea ingresar un producto? (si/no): ")
        if continuar.lower() != "si":
            break
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = int(input("Ingrese el precio del producto: "))
        stock_producto = 0
        if isinstance(tienda, Supermercado) or isinstance(tienda, Farmacia):
            stock_producto = int(input("Ingrese el stock del producto (opcional, default es 0): ") or 0)
        tienda.ingresar_producto(nombre_producto, precio_producto, stock_producto)

def main():
    tienda = crear_tienda()
    if tienda:
        ingresar_productos(tienda)
        while True:
            opcion = input("¿Qué desea hacer? (listar, vender, salir): ")
            if opcion.lower() == "listar":
                print(tienda.listar_productos())
            elif opcion.lower() == "vender":
                nombre_producto = input("Ingrese el nombre del producto a vender: ")
                cantidad = int(input("Ingrese la cantidad a vender: "))
                tienda.vender_producto(nombre_producto, cantidad)
            elif opcion.lower() == "salir":
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    main()