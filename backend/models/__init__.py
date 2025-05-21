from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# All models should be imported here to avoid circular imports
from models.compra import Compra
from models.contacto import Contacto
from models.enum import Enum
from models.explotacion import Explotacion
from models.historial_clinico import HistorialClinico
from models.parcela import Parcela
from models.produccion import Produccion
from models.raza import Raza
from models.res import Res
from models.usuario import Usuario
from models.venta import Venta