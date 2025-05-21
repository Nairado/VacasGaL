import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from models import db


class Parcela(db.Model):
    __tablename__ = 'parcela'

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_explotacion = db.Column(UUID(as_uuid=True), db.ForeignKey('explotacion.uuid'), nullable=False)
    uuid_produccion = db.Column(UUID(as_uuid=True), db.ForeignKey('produccion.uuid'), nullable=True)

    nombre = db.Column(db.String(120), nullable=False)
    ubicacion = db.Column(db.String(120), nullable=True)
    descripcion = db.Column(db.String(120), nullable=True)
    extension = db.Column(db.Float, nullable=False)
    arrendador = db.Column(db.String(120), nullable=True)
    coste_arrendamiento = db.Column(db.Float, nullable=True)
    
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    # Relationships
    explotacion = relationship('Explotacion', back_populates='parcelas')
    produccion = relationship('Produccion', backref='parcelas')
    reses = relationship('Res', back_populates='parcela', cascade='all, delete-orphan')
