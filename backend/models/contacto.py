import uuid
import enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from models import db
from models.enums import TipoContacto


class Contacto(db.Model):
    __tablename__ = 'contacto'

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_usuario = db.Column(UUID(as_uuid=True), db.ForeignKey('usuario.uuid'), nullable=False)

    tipo = db.Column(Enum(TipoContacto), nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    telefono = db.Column(db.String(120), nullable=True)
    direccion = db.Column(db.String(120), nullable=True)
    foto = db.Column(db.String(120), nullable=True)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    # Relationships
    compras = relationship('Compra', back_populates='contacto', cascade='all, delete-orphan')
    historiales = relationship('HistorialClinico', back_populates='contacto', cascade='all, delete-orphan')
    usuario = relationship('Usuario', back_populates='contactos')
    ventas = relationship('Venta', back_populates='contacto', cascade='all, delete-orphan')
