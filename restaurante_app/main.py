# main.py

# Importaciones modulares: conectando los diferentes archivos del proyecto
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    # 1. Crear el objeto principal que administrará el sistema
    mi_restaurante = Restaurante("El Rincón del Sabor")

    print("Iniciando sistema de gestión...\n")

    # 2. Crear objetos de la clase Producto
    p1 = Producto("Hamburguesa Clásica", 6.50, "Plato Fuerte")
    p2 = Producto("Limonada", 2.00, "Bebida")
    p3 = Producto("Tiramisú", 4.50, "Postre")

    # 3. Agregar los productos al restaurante
    mi_restaurante.registrar_producto(p1)
    mi_restaurante.registrar_producto(p2)
    mi_restaurante.registrar_producto(p3)

    # 4. Crear objetos de la clase Cliente
    c1 = Cliente("Jhocelyn del Pozo", "170000000")
    c2 = Cliente("Jose Andres", "0900000000")

    # 5. Registrar clientes en el restaurante
    mi_restaurante.registrar_cliente(c1)
    mi_restaurante.registrar_cliente(c2)

    # 6. Mostrar la información almacenada usando los métodos del servicio
    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()

# Condición para asegurar que el código solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    main()