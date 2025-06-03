from flask import Blueprint, request
from schemas.usuario import UsuarioCreate, UsuarioRead
from utils.validation import validate_body
from services.usuario_service import create_usuario_service, list_usuario_service

bp = Blueprint('usuario', __name__, url_prefix='/api/usuario')

@bp.route('', methods=['POST'])
@validate_body(UsuarioCreate)
def create_usuario(data: UsuarioCreate):
    usuario = create_usuario_service(data)
    return UsuarioRead.model_validate(usuario).model_dump(), 201


@bp.route('', methods=['GET'])
def list_usuario():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    filter = request.args.get('username', None)

    usuarios, total = list_usuario_service(page, per_page, filter)
    return {
        'usuarios': [UsuarioRead.model_validate(u).model_dump() for u in usuarios],
        'total': total,
        'page': page,
        'per_page': per_page
    }, 200
