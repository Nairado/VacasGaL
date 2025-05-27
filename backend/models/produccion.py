import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from models import db


class Produccion(db.Model):
    __tablename__ = 'produccion'

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_explotacion = db.Column(UUID(as_uuid=True), db.ForeignKey('explotacion.uuid'), nullable=False)
    
    tipo = db.Column(db.String(120), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    cantidad = db.Column(db.Float, nullable=True)

    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    # Relationships
    explotacion = relationship('Explotacion', back_populates='producciones')
    parcelas = relationship('Parcela', back_populates='produccion', cascade='all, delete-orphan')

