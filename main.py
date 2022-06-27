#from msilib import schema
from sqlite3 import dbapi2
import string
from typing import List
from tempfile import NamedTemporaryFile
import os
import csv

from fastapi import Depends, FastAPI, HTTPException, File , UploadFile
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

#CRUD test upload file


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    data = {}
    file_copy = NamedTemporaryFile(delete=False)
    
    try:
        with file_copy as f:  # The 'with' block ensures that the file closes and data are stored
            f.write(contents);
        
        with open(file_copy.name,'r', encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:             
                key = rows['No']
                data[key] = rows  
    finally:
        file_copy.close()  # Remember to close any file instances before removing the temp file
        os.unlink(file_copy.name)  # delete the file
    
    return data




#CRUD cho doi xe-----------------------------------

@app.post("/doixe/", tags=['doi xe'])
def create_doi_xe(doi_xe: schemas.Doi_xe_Create, db: Session = Depends(get_db)):
    return  crud.create_doi_xe(db=db, doi_xe = doi_xe )

@app.get("/doixe/", tags=['doi xe'])
def read_doi_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doi_xe = crud.get_all_doi_xe(db, skip=skip, limit=limit)
    return doi_xe

#Crud lay xe theo doi xe
@app.get("/doixe_xe/{id}", tags=['xe theo doi xe'])
def read_xe_theo_doi(id: int, skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    db_doi_xe = crud.get_xe_theo_doi_xe(db, id=id , skip=skip, limit=limit)
    return db_doi_xe

#Crud lay doi xe theo ten
@app.get("/doixe_ten/", tags=['doi xe theo ten'])
def read_doi_xe_theo_ten(ten_doi_xe: str , skip: int = 0, limit: int = 100 ,db: Session = Depends(get_db)):
    return crud.get_doi_xe_theo_ten(db, ten_doi_xe=ten_doi_xe)



@app.get("/doixe/{id}", tags=['doi xe'])
def read_doi_xe_id(id: int, db: Session = Depends(get_db)):
    db_doi_xe = crud.get_doi_xe(db, id=id)
    return db_doi_xe

@app.put("/update_doixe/{id}/", tags=['doi xe']) #id is a path parameter
def update_doi_xe(id:int, doi_xe:schemas.Doi_xe_Base, db:Session=Depends(get_db)):

    db_doi_xe = crud.get_doi_xe(db=db, id=id)

    if db_doi_xe:
        update_doi_xe = crud.update_doi_xe(db=db, id=id ,doi_xe=doi_xe)
        return update_doi_xe
    else:
        return {"error": f"doi xe voi id {id} khong ton tai"}

@app.delete("/xoa_doixe/{id}/", tags=['doi xe']) #id is a path parameter
def delete_doi_xe(id:int, db:Session=Depends(get_db)):

    db_doi_xe = crud.get_doi_xe(db=db, id=id)
    #check if friend object exists
    if db_doi_xe:
        return crud.delete_doi_xe(db=db, id=id)
    else:
        return {"error": f"doi xe voi id {id} khong ton tai"}
#Crud cho xe va tai  xe -------------------------------------------------------------------------------------------------------
@app.post("/xetaixe/",  tags=['create relationship xe tai xe'])
def create_xetaixe( xetaixe: schemas.Xe_taixe,  db: Session = Depends(get_db)):
    return crud.create_xetaixe(db=db, xetaixe=xetaixe)

"""
@app.get("/xe/")
def read_all_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    xe = crud.get_all_xetaixe(db, skip=skip, limit=limit)
    return xe


@app.get("/xe/{id}")
def read_xe_id(id: int, db: Session = Depends(get_db)):
    xe = crud.get_xetaixe(db, id=id)
    return xe
"""

#Crud cho xe -------------------------------------------------------------------------------------------------------
""" 
hint using this example to build endpoint for relationship column:

test update github master
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

@app.post("/xe/", tags=['xe'])
def create_xe( xe: schemas.Xe_Create,  db: Session = Depends(get_db)):
    return crud.create_xe(db=db, xe=xe)


@app.get("/xe/", tags=['xe'])
def read_all_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    xe = crud.get_all_xe(db, skip=skip, limit=limit)
    return xe


@app.get("/xe/{id}", tags=['xe'])
def read_xe_id(id: int, db: Session = Depends(get_db)):
    xe = crud.get_xe(db, id=id)
    return xe


@app.put("/update_xe/{id}/", tags=['xe']) #id is a path parameter
def update_xe(id: int ,xe: schemas.Xe_Base, db:Session=Depends(get_db)):

    db_xe = crud.get_xe(db=db, id=id)

    if db_xe:
        update_xe = crud.update_xe(db=db, xe=xe, id=id)
        return update_xe
    else:
        return {"error": f"xe voi id {id} khong ton tai"}


@app.delete("/xoa_xe/{id}/", tags=['xe']) #id is a path parameter
def delete_xe(id:int, db:Session=Depends(get_db)):

    db_xe = crud.get_xe(db=db, id=id)

    if db_xe:
        return crud.delete_xe(db=db, id=id)
    else:
        return {"error": f"xe voi id {id} khong ton tai"}

#CRUD cho tai xe----------------------------------------

@app.post("/taixe/", tags=['tai xe'])
def create_tai_xe(tai_xe: schemas.Tai_xe_Create, db: Session = Depends(get_db)):
    return crud.create_tai_xe(db=db, tai_xe = tai_xe )


@app.get("/taixe/", tags=['tai xe'])
def read_tai_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tai_xe = crud.get_all_tai_xe(db, skip=skip, limit=limit)
    return tai_xe


@app.get("/taixe/{id}", tags=['tai xe'])
def read_tai_xe_id(id: int, db: Session = Depends(get_db)):
    tai_xe = crud.get_tai_xe(db, id=id)
    return tai_xe

#Crud lay chuyen xe theo tai xe
@app.get("/taixe_chuyenxe/{id}", tags=['lay chuyen xe theo tai xe'])
def read_chuyen_xe_theo_tai_xe(id: int, skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    db_chuyenxe = crud.get_chuyenxe_theo_tai_xe(db, id=id , skip=skip, limit=limit)
    return db_chuyenxe

@app.put("/update_taixe/{id}/", tags=['tai xe']) #id is a path parameter
def update_tai_xe(id:int, tai_xe:schemas.Tai_xe_Base, db:Session=Depends(get_db)):

    db_tai_xe = crud.get_tai_xe(db=db, id=id)

    if db_tai_xe:
        update_tai_xe = crud.update_tai_xe(db=db, id=id ,tai_xe = tai_xe)
        return update_tai_xe
    else:
        return {"error": f"tai xe voi id {id} khong ton tai"}


@app.delete("/xoa_taixe/{id}/", tags=['tai xe']) #id is a path parameter
def delete_tai_xe(id:int, db:Session=Depends(get_db)):

    db_tai_xe = crud.get_tai_xe(db=db, id=id)

    if db_tai_xe:
        return crud.delete_tai_xe(db=db, id=id)
    else:
        return {"error": f"tai xe voi id {id} khong ton tai"}

#Crud cho chuyen xe ---------------------------

@app.post("/chuyenxe/", tags=['chuyen xe'])
def create_chuyen_xe(chuyen_xe: schemas.Chuyen_xe_Create, db: Session = Depends(get_db)):
    return crud.create_chuyen_xe(db=db, chuyen_xe = chuyen_xe )


@app.get("/chuyenxe/", tags=['chuyen xe'])
def read_chuyen_xe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    chuyen_xe = crud.get_all_chuyen_xe(db, skip=skip, limit=limit)
    return chuyen_xe


@app.get("/chuyenxe/{id}", tags=['chuyen xe'])
def read_chuyen_xe_id(id: int, db: Session = Depends(get_db)):
    chuyen_xe = crud.get_chuyen_xe(db, id=id)
    return chuyen_xe


@app.put("/update_chuyenxe/{id}/", tags=['chuyen xe']) #id is a path parameter
def update_chuyen_xe ( id:int, chuyenxe: schemas.Chuyen_xe_Base, db:Session=Depends(get_db)):

    db_chuyen_xe = crud.get_chuyen_xe(db=db, id=id)

    if db_chuyen_xe:
        update_chuyen_xe = crud.update_chuyen_xe(db=db, id=id, chuyenxe = chuyenxe)
        return update_chuyen_xe
    else:
        return {"error": f"chuyen xe voi id {id} khong ton tai"}


@app.delete("/xoa_chuyenxe/{id}/", tags=['chuyen xe']) #id is a path parameter
def delete_chuyen_xe(id:int, db:Session=Depends(get_db)):

    db_chuyen_xe = crud.get_chuyen_xe(db=db, id=id)

    if db_chuyen_xe:
        return crud.delete_chuyen_xe(db=db, id=id)
    else:
        return {"error": f"chuyen xe voi id {id} khong ton tai"}
