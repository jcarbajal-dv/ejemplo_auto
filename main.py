from typing import Optional

class Vehiculo:
    def __init__(self, tipo_combustible: str, numero_ruedas: int):
        self.tipo_combustible = tipo_combustible
        self.numero_ruedas = numero_ruedas
    
    def descripcion(self) -> str:
        return f"Este vehículo tiene {self.numero_ruedas} ruedas y usa {self.tipo_combustible} como combustible."

# Subclase Automovil, hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, tipo_combustible: str, numero_ruedas: int, tipo: str):
        super().__init__(tipo_combustible, numero_ruedas)
        self.tipo = tipo  # Tipo de automovil (Sedan o SUV)
    
    def descripcion(self) -> str:
        base_desc = super().descripcion()
        return f"{base_desc} Es un automóvil tipo {self.tipo}."

# Subclase Motocicleta, hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, tipo_combustible: str, numero_ruedas: int, cilindrada: Optional[int] = None):
        super().__init__(tipo_combustible, numero_ruedas)
        self.cilindrada = cilindrada  # Cilindrada de la motocicleta
    
    def descripcion(self) -> str:
        base_desc = super().descripcion()
        if self.cilindrada:
            return f"{base_desc} Tiene una cilindrada de {self.cilindrada} cc."
        return base_desc

# Subclase Camion, hereda de Vehiculo
class Camion(Vehiculo):
    def __init__(self, tipo_combustible: str, numero_ruedas: int, capacidad_carga: float):
        super().__init__(tipo_combustible, numero_ruedas)
        self.capacidad_carga = capacidad_carga  # Capacidad de carga del camión en toneladas
    
    def descripcion(self) -> str:
        base_desc = super().descripcion()
        return f"{base_desc} Tiene una capacidad de carga de {self.capacidad_carga} toneladas."

# Crear instancias de los vehículos

# Automóvil Sedan
sedan = Automovil(tipo_combustible="Gasolina", numero_ruedas=4, tipo="Sedan")

# Automóvil SUV
suv = Automovil(tipo_combustible="Diesel", numero_ruedas=4, tipo="SUV")

# Motocicleta
motocicleta = Motocicleta(tipo_combustible="Gasolina", numero_ruedas=2, cilindrada=150)

# Camión
camion = Camion(tipo_combustible="Diesel", numero_ruedas=6, capacidad_carga=15)

# Imprimir descripciones
print(sedan.descripcion())
print(suv.descripcion())
print(motocicleta.descripcion())
print(camion.descripcion())