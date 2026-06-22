class Cliente:
    """Clase que representa a un cliente del restaurante."""
    
    def __init__(self, cedula: str, nombre: str):
        self.cedula = cedula
        self.nombre = nombre

    def __str__(self):
        # Método especial para representar al cliente
        return f"Cliente: {self.nombre} (Cédula: {self.cedula})"