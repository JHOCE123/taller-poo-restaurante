
class Restaurante:
    """Clase de servicio que gestiona la lógica del restaurante."""
    
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.menu = []        # Lista para almacenar objetos de tipo Producto
        self.clientes = []    # Lista para almacenar objetos de tipo Cliente

    def registrar_producto(self, producto: Producto):
        """Agrega un objeto Producto a la lista del menú."""
        self.menu.append(producto)
        print(f"✔ Producto '{producto.nombre}' agregado al menú.")

    def registrar_cliente(self, cliente: Cliente):
        """Agrega un objeto Cliente al registro del restaurante."""
        self.clientes.append(cliente)
        print(f"✔ Cliente '{cliente.nombre}' registrado con éxito.")

    def mostrar_menu(self):
        """Muestra en consola todos los productos registrados."""
        print(f"\n--- MENÚ DE {self.nombre.upper()} ---")
        if not self.menu:
            print("El menú está vacío.")
        for prod in self.menu:
            print(prod)  # Llama automáticamente al __str__ de la clase Producto

    def mostrar_clientes(self):
        """Muestra en consola todos los clientes registrados."""
        print("\n--- CLIENTES REGISTRADOS ---")
        if not self.clientes:
            print("No hay clientes registrados.")
        for cli in self.clientes:
            print(cli)  # Llama automáticamente al __str__ de la clase Cliente