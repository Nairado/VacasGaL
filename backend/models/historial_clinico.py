import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from models import db


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

    # Relationships
    res = relationship('Res', back_populates='historiales_clinicos')
    contacto = relationship('Contacto', back_populates='historiales_clinicos')
