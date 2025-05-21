from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from models import db


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

    # Relationships
    contactos = relationship('Contacto', back_populates='usuario', cascade='all, delete-orphan')
    explotaciones = relationship('Explotacion', back_populates='usuario', cascade='all, delete-orphan')
