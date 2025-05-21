import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import Enum
from models import db
from models.enums import Especie, Sexo


class Res(db.Model):
    __tablename__ = 'res'

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    uuid_explotacion = db.Column(UUID(as_uuid=True), db.ForeignKey('explotacion.uuid'), nullable=False)
    uuid_progenitor = db.Column(UUID(as_uuid=True), db.ForeignKey('res.uuid'), nullable=True)
    uuid_progenitora = db.Column(UUID(as_uuid=True), db.ForeignKey('res.uuid'), nullable=True)
    uuid_parcela = db.Column(UUID(as_uuid=True), db.ForeignKey('parcela.uuid'), nullable=True)
    raza_id = db.Column(UUID(as_uuid=True), db.ForeignKey('raza.uuid'), nullable=True)
    compra_id = db.Column(UUID(as_uuid=True), db.ForeignKey('compra.uuid'), nullable=True)
    venta_id = db.Column(UUID(as_uuid=True), db.ForeignKey('venta.uuid'), nullable=True)

    nombre = db.Column(db.String(120), nullable=True)
    especie = db.Column(Enum(Especie), nullable=False)
    sexo = db.Column(Enum(Sexo), nullable=False)
    peso = db.Column(db.Float, nullable=True)
    fecha_nacimiento = db.Column(db.DateTime, nullable=True)
    fecha_deceso = db.Column(db.DateTime, nullable=True)
    celo = db.Column(db.Boolean, nullable=True)
    fecha_ultimo_parto = db.Column(db.DateTime, nullable=True)
    fecha_preñez = db.Column(db.DateTime, nullable=True)
    numero_identificacion = db.Column(db.String(120), nullable=True)
    foto = db.Column(db.String(120), nullable=True)

    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    # Relationships
    explotacion = relationship('Explotacion', back_populates='reses')
    parcela = relationship('Parcela', back_populates='reses')
    raza = relationship('Raza', back_populates='reses')
    compra = relationship('Compra', back_populates='reses')
    venta = relationship('Venta', back_populates='reses')
    historiales = relationship('HistorialClinico', back_populates='res', cascade='all, delete-orphan')

    # Self-referential relationships
    progenitor = relationship('Res', remote_side=[uuid], foreign_keys=[uuid_progenitor], post_update=True, backref='crias_macho')
    progenitora = relationship('Res', remote_side=[uuid], foreign_keys=[uuid_progenitora], post_update=True, backref='crias_hembra')
