from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from model import Base

ModelClass = TypeVar("ModelClass", bound=Base)
CreateSchemaClass = TypeVar("CreateSchemaClass", bound=BaseModel)
UpdateSchemaClass = TypeVar("UpdateSchemaClass", bound=BaseModel)


class Crud(Generic[ModelClass, CreateSchemaClass, UpdateSchemaClass]):
    def __init__(self, db: Session, model_class: type[ModelClass]):
        self.__model_class = model_class
        self._db = db

    def create(self, db_in: CreateSchemaClass) -> ModelClass:
        db_obj = self.__model_class(**db_in.model_dump())
        self._db.add(db_obj)
        self._db.commit()
        return db_obj

    def update(self, db_in: CreateSchemaClass, db_obj: ModelClass) -> ModelClass:
        for key, value in db_in.model_dump(exclude_unset=True).items():
            setattr(db_obj, key, value)
        self._db.commit()
        self._db.refresh(db_obj)
        return db_obj

    def delete(self, ident: int) -> ModelClass | None:
        db_obj = self._db.get(self.__model_class, ident)
        if db_obj:
            self._db.delete(db_obj)
            self._db.commit()
        return db_obj

    def get(self, ident: int) -> ModelClass | None:
        return self._db.get(self.__model_class, ident)
