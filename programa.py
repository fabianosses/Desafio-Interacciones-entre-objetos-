from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

tiendas = []

def agregar_tienda():
    print("""
          --- Agregar Nueva Tienda ---
            Seleccione el tipo de tienda:
            1. Restaurante
            2. Supermercado
            3. Farmacia
            4. Salir
          """)

    while True:

        opcion = input("Ingrese el número de opción: ")
        if opcion == '1':
            nombre = input("Ingrese el nombre del Restaurante: ")
            delivery = input(" Ingrese precio Delivery: ")
            return tiendas.append(Restaurante(nombre, delivery))
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del Supermercado: ")
            delivery = input(" Ingrese precio Delivery: ")
            return tiendas.append(Supermercado(nombre, delivery))
        
        elif opcion == '3':
            nombre = input("Ingrese el nombre de la Farmacia: ")
            delivery = input(" Ingrese precio Delivery: ")
            return tiendas.append(Farmacia(nombre, delivery))
        
        elif opcion == '4':
            return None
        else:
            print("Opción inválida. Intente de nuevo.")

# Agregar tiendas existentes

agregar_tienda()
