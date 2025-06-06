from extensions import db
from uuid import uuid4, UUID

from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioUpdate


def create_usuario_service(data: UsuarioCreate):
    nuevo_usuario = Usuario(
        uuid=uuid4(),
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


def delete_usuario_service(usuario_id: UUID):
    usuario = Usuario.query.filter_by(uuid=usuario_id).first()
    if not usuario:
        return False

    db.session.delete(usuario)
    db.session.commit()
    return True


def get_usuario_service(uuid: UUID):
    return Usuario.query.filter_by(uuid=uuid).first()


def list_usuario_service(page: int, per_page: int, username: str = None):
    query = Usuario.query

    if username:
        query = query.filter(Usuario.username.ilike(f"%{username}%"))

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    return pagination.items, pagination.total


def update_usuario_service(usuario_id: UUID, data: UsuarioUpdate):
    usuario = Usuario.query.filter_by(uuid=usuario_id).first()
    if not usuario:
        return None

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(usuario, field, value)

    db.session.commit()
    return usuario