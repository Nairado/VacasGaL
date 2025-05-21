import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from models import db


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

    # Relationships
    usuario = relationship('Usuario', back_populates='explotaciones')
    producciones = relationship('Produccion', back_populates='explotacion', cascade='all, delete-orphan')
    parcelas = relationship('Parcela', back_populates='explotacion', cascade='all, delete-orphan')
    reses = relationship('Res', back_populates='explotacion', cascade='all, delete-orphan')
