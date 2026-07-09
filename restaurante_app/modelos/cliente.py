"""Modelo que representa a un cliente del restaurante."""

from dataclasses import dataclass


@dataclass
class Cliente:
    """Cliente registrado en el sistema del restaurante."""

    nombre: str
    correo: str
    id_cliente: str

    def mostrar_informacion(self):
        """Devuelve una descripción legible del cliente."""
        return f"{self.id_cliente} - {self.nombre} ({self.correo})"
