
# modelos/producto.py

class Producto:
    def __init__(self, nombre, precio, categoria):
        """
        Constructor de la clase Producto.
        Inicializa los atributos básicos de un ítem del menú.
        """
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        """
        Método especial para representar el objeto como una cadena de texto.
        Facilita la impresión del producto en consola.
        """
        return f"[{self.categoria}] {self.nombre} - ${self.precio:.2f}"
   