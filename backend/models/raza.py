import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from models import db


class Raza(db.Model):
    __tablename__ = 'raza'

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    nombre = db.Column(db.String(120), unique=True, nullable=False)
    descripcion = db.Column(db.String(120), nullable=True)
    foto = db.Column(db.String(120), nullable=True)

    # Relationships
    reses = relationship('Res', back_populates='raza', cascade='all, delete-orphan')
