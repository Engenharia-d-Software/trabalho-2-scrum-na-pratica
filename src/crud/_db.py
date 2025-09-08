from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

_engine = create_engine("sqlite://")
_session_builder = sessionmaker(bind=_engine, autocommit=False, autoflush=False, class_=Session)

@lru_cache(maxsize=1) # apply a singleton behavior to the get_session function automatically
def get_session():
    return _session_builder()

def create_all(base_class: DeclarativeBase):
    base_class.metadata.create_all(bind=_engine)
