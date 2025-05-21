import enum

class TipoContacto(enum.Enum):
    CLIENTE = 'cliente'
    PROVEEDOR = 'proveedor'
    VETERINARIO = 'veterinario'
    OTRO = 'otro'

class Sexo(enum.Enum):
    MACHO = 'macho'
    HEMBRA = 'hembra'

class Especie(enum.Enum):
    BOVINO = 'bovino'
    OVINO = 'ovino'
    CAPRINO = 'caprino'
    PORCINO = 'porcino'
    EQUINO = 'equino'
    AVICOLA = 'avícola'
    CONEJO = 'conejo'
    OTRO = 'otro'
