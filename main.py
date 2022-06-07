from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from  database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#CRUD cho doi xe

@app.post("/doixe/", response_model=schemas.Doi_xe)
def create_doi_xe(doi_xe: schemas.Doi_xe_Create, db: Session = Depends(get_db)):
    return crud.create_doi_xe(db=db, doi_xe = doi_xe )


@app.get("/doixe/", response_model=List[schemas.Doi_xe])
def read_doi_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doi_xe = crud.get_all_doi_xe(db, skip=skip, limit=limit)
    return doi_xe


#dang code cho nay
@app.get("/doixe_xe/{id}", response_model=List[schemas.Doi_xe])
def read_xe_theo_doi(id: int, skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    db_doi_xe = crud.get_xe_theo_doi_xe(db, id=id , skip=skip, limit=limit)
    return db_doi_xe


@app.get("/doixe/{id}", response_model=schemas.Doi_xe)
def read_doi_xe_id(id: int, db: Session = Depends(get_db)):
    db_doi_xe = crud.get_doi_xe(db, id=id)
    return db_doi_xe



@app.put("/update_doixe/{id}/") #id is a path parameter
def update_doi_xe(id:int, ten_doi_xe:str, db:Session=Depends(get_db)):

    db_doi_xe = crud.get_doi_xe(db=db, id=id)

    if db_doi_xe:
        update_doi_xe = crud.update_doi_xe(db=db, id=id ,ten_doi_xe = ten_doi_xe)
        return update_doi_xe
    else:
        return {"error": f"doi xe voi id {id} khong ton tai"}


@app.delete("/xoa_doixe/{id}/") #id is a path parameter
def delete_doi_xe(id:int, db:Session=Depends(get_db)):

    db_doi_xe = crud.get_doi_xe(db=db, id=id)
    #check if friend object exists
    if db_doi_xe:
        return crud.delete_doi_xe(db=db, id=id)
    else:
        return {"error": f"doi xe voi id {id} khong ton tai"}



#Crud cho xe


@app.post("/xe/", response_model=schemas.Xe)
def create_xe( doi_xe_id: int ,  xe: schemas.Xe_Create, db: Session = Depends(get_db)):
    return crud.create_xe(db=db, xe = xe , doi_xe_id = doi_xe_id  )


@app.get("/xe/", response_model=List[schemas.Xe])
def read_all_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    xe = crud.get_all_xe(db, skip=skip, limit=limit)
    return xe


@app.get("/xe/{id}", response_model=schemas.Xe)
def read_xe_id(id: int, db: Session = Depends(get_db)):
    xe = crud.get_xe(db, id=id)
    return xe


@app.put("/update_xe/{id}/") #id is a path parameter
def update_xe(id:int, ten_xe:str, db:Session=Depends(get_db)):

    db_xe = crud.get_xe(db=db, id=id)

    if db_xe:
        update_xe = crud.update_xe(db=db, id=id , ten_xe = ten_xe)
        return update_xe
    else:
        return {"error": f"xe voi id {id} khong ton tai"}


@app.delete("/xoa_xe/{id}/") #id is a path parameter
def delete_xe(id:int, db:Session=Depends(get_db)):

    db_xe = crud.get_xe(db=db, id=id)

    if db_xe:
        return crud.delete_xe(db=db, id=id)
    else:
        return {"error": f"xe voi id {id} khong ton tai"}

#CRUD cho tai xe

@app.post("/taixe/", response_model=schemas.Tai_xe)
def create_tai_xe(tai_xe: schemas.Tai_xe_Create, db: Session = Depends(get_db)):
    return crud.create_tai_xe(db=db, tai_xe = tai_xe )


@app.get("/taixe/", response_model=List[schemas.Tai_xe])
def read_tai_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tai_xe = crud.get_all_tai_xe(db, skip=skip, limit=limit)
    return tai_xe


@app.get("/taixe/{id}", response_model=schemas.Tai_xe)
def read_tai_xe_id(id: int, db: Session = Depends(get_db)):
    tai_xe = crud.get_tai_xe(db, id=id)
    return tai_xe


@app.put("/update_taixe/{id}/") #id is a path parameter
def update_tai_xe(id:int, ten_tai_xe:str, db:Session=Depends(get_db)):

    db_tai_xe = crud.get_tai_xe(db=db, id=id)

    if db_tai_xe:
        update_tai_xe = crud.update_tai_xe(db=db, id=id ,ten_tai_xe = ten_tai_xe)
        return update_tai_xe
    else:
        return {"error": f"tai xe voi id {id} khong ton tai"}


@app.delete("/xoa_taixe/{id}/") #id is a path parameter
def delete_tai_xe(id:int, db:Session=Depends(get_db)):

    db_tai_xe = crud.get_tai_xe(db=db, id=id)

    if db_tai_xe:
        return crud.delete_tai_xe(db=db, id=id)
    else:
        return {"error": f"tai xe voi id {id} khong ton tai"}

#Crud cho chuyen xe

@app.post("/chuyenxe/", response_model=schemas.Chuyen_xe)
def create_chuyen_xe(chuyen_xe: schemas.Chuyen_xe_Create, db: Session = Depends(get_db)):
    return crud.create_chuyen_xe(db=db, chuyen_xe = chuyen_xe )


@app.get("/chuyenxe/", response_model=List[schemas.Chuyen_xe])
def read_chuyen_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    chuyen_xe = crud.get_all_chuyen_xe(db, skip=skip, limit=limit)
    return chuyen_xe


@app.get("/chuyenxe/{id}", response_model=schemas.Tai_xe)
def read_chuyen_xe_id(id: int, db: Session = Depends(get_db)):
    chuyen_xe = crud.get_chuyen_xe(db, id=id)
    return chuyen_xe


@app.put("/update_chuyenxe/{id}/") #id is a path parameter
def update_chuyen_xe ( id:int, ten_chuyen_xe:str, db:Session=Depends(get_db)):

    db_chuyen_xe = crud.get_chuyen_xe(db=db, id=id)

    if db_chuyen_xe:
        update_chuyen_xe = crud.update_chuyen_xe(db=db, id=id, ten_chuyen_xe = ten_chuyen_xe)
        return update_chuyen_xe
    else:
        return {"error": f"chuyen xe voi id {id} khong ton tai"}


@app.delete("/xoa_chuyenxe/{id}/") #id is a path parameter
def delete_chuyen_xe(id:int, db:Session=Depends(get_db)):

    db_chuyen_xe = crud.get_chuyen_xe(db=db, id=id)

    if db_chuyen_xe:
        return crud.delete_chuyen_xe(db=db, id=id)
    else:
        return {"error": f"chuyen xe voi id {id} khong ton tai"}
