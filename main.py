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

#CRUD cho doi xe-----------------------------------

@app.post("/doixe/")
def create_doi_xe(doi_xe: schemas.Doi_xe_Create, db: Session = Depends(get_db)):
    return crud.create_doi_xe(db=db, doi_xe = doi_xe )


@app.get("/doixe/")
def read_doi_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doi_xe = crud.get_all_doi_xe(db, skip=skip, limit=limit)
    return doi_xe


#Crud lay xe theo doi xe
@app.get("/doixe_xe/{id}")
def read_xe_theo_doi(id: int, skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    db_doi_xe = crud.get_xe_theo_doi_xe(db, id=id , skip=skip, limit=limit)
    return db_doi_xe


@app.get("/doixe/{id}")
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



#Crud cho xe -------------------------------------------------------------------------------------------------------
"""
using this example to build endpoint for relationship column:
https://stackoverflow.com/questions/68394091/fastapi-sqlalchemy-pydantic-%E2%86%92-how-to-process-many-to-many-relations

def create_article(db: Session, article_data: schema.ArticleCreate):
    db_article = model.Article(subject=article_data.subject, text=article_data.text)
    if (editors := db.query(model.Editor).filter(model.Editor.id.in_(article_data.editor_ids))).count() == len(endpoint_data.topic_ids):
        db_article.topics.extend(editors)
    else:
        # even if at least one editor is not found, an error is raised
        # if existence is not matter you can skip this check and add relations only for existing data
        raise HTTPException(status_code=404, detail="editor not found")
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
"""

@app.post("/xe/")
def create_xe( doi_xe_id: int, xe_tai_xe: List, xe: schemas.Xe_Create,  db: Session = Depends(get_db)):
    return crud.create_xe(db=db, xe=xe, doi_xe_id=doi_xe_id,xe_tai_xe=xe_tai_xe)


@app.get("/xe/")
def read_all_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    xe = crud.get_all_xe(db, skip=skip, limit=limit)
    return xe


@app.get("/xe/{id}")
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

#CRUD cho tai xe----------------------------------------

@app.post("/taixe/")
def create_tai_xe(tai_xe_chuyen_xe : List, tai_xe: schemas.Tai_xe_Create, db: Session = Depends(get_db)):
    return crud.create_tai_xe(db=db, tai_xe = tai_xe, tai_xe_chuyen_xe=tai_xe_chuyen_xe )


@app.get("/taixe/")
def read_tai_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tai_xe = crud.get_all_tai_xe(db, skip=skip, limit=limit)
    return tai_xe


@app.get("/taixe/{id}")
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

#Crud cho chuyen xe ---------------------------

@app.post("/chuyenxe/")
def create_chuyen_xe(chuyen_xe: schemas.Chuyen_xe_Create, db: Session = Depends(get_db)):
    return crud.create_chuyen_xe(db=db, chuyen_xe = chuyen_xe )


@app.get("/chuyenxe/")
def read_chuyen_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    chuyen_xe = crud.get_all_chuyen_xe(db, skip=skip, limit=limit)
    return chuyen_xe


@app.get("/chuyenxe/{id}")
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
