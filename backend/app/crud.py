from sqlalchemy.orm import Session
from app.models import Dua
from app.schemas import DuaCreate

# Create a new Dua


def create_dua(db: Session, dua: DuaCreate):
    db_dua = Dua(title=dua.title, content=dua.content)
    db.add(db_dua)
    db.commit()
    db.refresh(db_dua)
    return db_dua

# Read all Duas


def get_duas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Dua).offset(skip).limit(limit).all()
