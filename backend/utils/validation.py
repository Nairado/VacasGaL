from flask import request
from pydantic import BaseModel, ValidationError
from typing import Type


def validate_body(schema: Type[BaseModel]):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            try:
                data = schema.model_validate(request.json)
                return fn(*args, **kwargs, data=data)
            except ValidationError as e:
                return {"error": e.errors()}, 422
        wrapper.__name__ = fn.__name__
        return wrapper
    return decorator