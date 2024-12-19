from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

# Initialize FastAPI app
app = FastAPI()

# Define a simple route


@app.get("/")
def read_root():
    return {"message": "Welcome to the Dua API"}


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API to create a new Dua


@app.post("/duas/", response_model=schemas.DuaResponse)
def create_dua(dua: schemas.DuaCreate, db: Session = Depends(get_db)):
    return crud.create_dua(db=db, dua=dua)

# API to get all Duas


@app.get("/duas/", response_model=list[schemas.DuaResponse])
def read_duas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_duas(db=db, skip=skip, limit=limit)


@app.get("/duas/{dua_id}", response_model=schemas.DuaResponse)
def get_dua_by_id(dua_id: int, db: Session = Depends(get_db)):
    dua = db.query(Dua).filter(Dua.id == dua_id).first()
    if not dua:
        raise HTTPException(status_code=404, detail="Dua not found")
    return dua


@app.put("/duas/{dua_id}", response_model=schemas.DuaResponse)
def update_dua(dua_id: int, dua: schemas.DuaCreate, db: Session = Depends(get_db)):
    db_dua = db.query(Dua).filter(Dua.id == dua_id).first()
    if not db_dua:
        raise HTTPException(status_code=404, detail="Dua not found")
    db_dua.title = dua.title
    db_dua.content = dua.content
    db.commit()
    db.refresh(db_dua)
    return db_dua


@app.delete("/duas/{dua_id}")
def delete_dua(dua_id: int, db: Session = Depends(get_db)):
    db_dua = db.query(Dua).filter(Dua.id == dua_id).first()
    if not db_dua:
        raise HTTPException(status_code=404, detail="Dua not found")
    db.delete(db_dua)
    db.commit()
    return {"message": "Dua deleted successfully"}
