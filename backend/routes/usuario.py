from flask import Blueprint
from schemas.usuario import UsuarioCreate, UsuarioRead
from utils.validation import validate_body
from services.usuario_service import create_usuario_service

bp = Blueprint('usuario', __name__, url_prefix='/api/usuarios')

@bp.route('', methods=['POST'])
@validate_body(UsuarioCreate)
def crear_usuario(data: UsuarioCreate):
    usuario = create_usuario_service(data)
    return UsuarioRead.model_validate(usuario).model_dump(), 201
