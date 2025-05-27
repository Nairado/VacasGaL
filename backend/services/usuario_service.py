from models.usuario import Usuario
from extensions import db
import uuid

def create_usuario_service(data):
    nuevo_usuario = Usuario(
        uuid=uuid.uuid4(),
        username=data.username,
        nombre=data.nombre,
        apellido=data.apellido,
        email=data.email,
        password=data.password,  # It have to be hashed!
        ubicacion=data.ubicacion,
        telefono=data.telefono,
        foto=data.foto
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario
