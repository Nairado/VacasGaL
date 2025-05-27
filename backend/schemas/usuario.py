from schemas.base import CamelModel
from pydantic import EmailStr, constr
from typing import Optional
from uuid import UUID
from datetime import datetime

class UsuarioCreate(CamelModel):
    username: constr(min_length=3, max_length=80)
    nombre: str
    apellido: str
    email: EmailStr
    password: str
    ubicacion: str
    telefono: Optional[str] = None
    foto: Optional[str] = None

class UsuarioRead(CamelModel):
    uuid: UUID
    username: str
    nombre: str
    apellido: str
    email: EmailStr
    ubicacion: str
    telefono: Optional[str]
    foto: Optional[str]
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        from_attributes = True
