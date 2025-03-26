import uuid
import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import UUID


db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(80), unique=True, nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    ubicacion = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(120), nullable=True)
    foto = db.Column(db.String(120), nullable=True)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


class TipoContacto(enum.Enum):
    CLIENTE = 'cliente'
    PROVEEDOR = 'proveedor'
    VETERINARIO = 'veterinario'
    OTRO = 'otro'


class Contacto(db.Model):
    __tablename__ = 'contacto'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tipo = db.Column(Enum(TipoContacto), nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    telefono = db.Column(db.String(120), nullable=True)
    direccion = db.Column(db.String(120), nullable=True)
    foto = db.Column(db.String(120), nullable=True)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


class Explotacion(db.Model):
    __tablename__ = 'explotacion'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_usuario = db.Column(UUID(as_uuid=True), db.ForeignKey('usuario.uuid'), nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    ubicacion = db.Column(db.String(120), nullable=True)
    descripcion = db.Column(db.String(120), nullable=True)
    foto = db.Column(db.String(120), nullable=True)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


class Produccion(db.Model):
    __tablename__ = 'produccion'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_explotacion = db.Column(UUID(as_uuid=True), db.ForeignKey('explotacion.uuid'), nullable=False)
    tipo = db.Column(db.String(120), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    cantidad = db.Column(db.Float, nullable=True)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


class Pasture(db.Model):
    __tablename__ = 'parcela'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_explotacion = db.Column(UUID(as_uuid=True), db.ForeignKey('explotacion.uuid'), nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    ubicacion = db.Column(db.String(120), nullable=True)
    descripcion = db.Column(db.String(120), nullable=True)
    extension = db.Column(db.Float, nullable=False)
    arrendador = db.Column(db.String(120), nullable=True)
    coste_arrendamiento = db.Column(db.Float, nullable=True)
    uuid_produccion = db.Column(UUID(as_uuid=True), db.ForeignKey('produccion.uuid'), nullable=True)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


class HistorialClinico(db.Model):
    __tablename__ = 'historial_clinico'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_res = db.Column(UUID(as_uuid=True), db.ForeignKey('res.uuid'), nullable=False)
    uuid_contacto = db.Column(UUID(as_uuid=True), db.ForeignKey('contacto.uuid'), nullable=True)
    fecha = db.Column(db.DateTime, nullable=False)
    motivo = db.Column(db.String(120), nullable=True)
    diagnostico = db.Column(db.String(120), nullable=True)
    tratamiento = db.Column(db.String(120), nullable=True)
    coste = db.Column(db.Float, nullable=True)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


class Compra(db.Model):
    __tablename__ = 'compra'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_contacto = db.Column(UUID(as_uuid=True), db.ForeignKey('contacto.uuid'), nullable=True)
    precio = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)


class Venta(db.Model):
    __tablename__ = 'venta'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_contacto = db.Column(UUID(as_uuid=True), db.ForeignKey('contacto.uuid'), nullable=True)
    precio = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)


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


class Raza(db.Model):
    __tablename__ = 'raza'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    descripcion = db.Column(db.String(120), nullable=True)
    foto = db.Column(db.String(120), nullable=True)


class Res(db.Model):
    __tablename__ = 'res'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_explotacion = db.Column(UUID(as_uuid=True), db.ForeignKey('explotacion.uuid'), nullable=False)
    uuid_progenitor = db.Column(UUID(as_uuid=True), nullable=True)
    uuid_progenitora = db.Column(UUID(as_uuid=True), nullable=True)
    uuid_parcela = db.Column(UUID(as_uuid=True), db.ForeignKey('parcela.uuid'), nullable=True)
    nombre = db.Column(db.String(120), nullable=True)
    especie = db.Column(Enum(Especie), nullable=False)
    raza = db.Column(UUID(as_uuid=True), db.ForeignKey('raza.uuid'), nullable=True)
    sexo = db.Column(Enum(Sexo), nullable=False)
    peso = db.Column(db.Float, nullable=True)
    fecha_nacimiento = db.Column(db.DateTime, nullable=True)
    fecha_deceso = db.Column(db.DateTime, nullable=True)
    celo = db.Column(db.Boolean, nullable=True)
    fecha_ultimo_parto = db.Column(db.DateTime, nullable=True)
    fecha_preñez = db.Column(db.DateTime, nullable=True)
    numero_identificacion = db.Column(db.String(120), nullable=True)
    compra = db.Column(UUID(as_uuid=True), db.ForeignKey('compra.uuid'), nullable=True)
    venta = db.Column(UUID(as_uuid=True), db.ForeignKey('venta.uuid'), nullable=True)
    foto = db.Column(db.String(120), nullable=True)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


