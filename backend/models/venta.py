import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from models import db


class Venta(db.Model):
    __tablename__ = 'venta'

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_contacto = db.Column(UUID(as_uuid=True), db.ForeignKey('contacto.uuid'), nullable=True)

    precio = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    # Relationships
    contacto = relationship('Contacto', back_populates='ventas')
    reses = relationship('Res', back_populates='venta', cascade='all, delete-orphan')