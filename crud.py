import string
from typing import List
from sqlalchemy.orm import Session

import models, schemas

#crud cho doi xe

def get_doi_xe(db: Session, id: int):
    return db.query(models.Doi_xe).filter(models.Doi_xe.id == id).first()

#Crud lay doi xe theo ten

def get_doi_xe_theo_ten(db:Session, ten_doi_xe:str, skip: int = 0, limit: int = 100):
    return db.query(models.Doi_xe).filter(models.Doi_xe.ten_doi_xe==ten_doi_xe).all()

#lay xe theo doi xe
def get_xe_theo_doi_xe(db: Session, id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Doi_xe,models.Xe).filter(models.Doi_xe.id==models.Xe.doi_xe_id).filter(models.Doi_xe.id == id).all()

def get_all_doi_xe(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doi_xe).offset(skip).limit(limit).all()


def create_doi_xe(db: Session, doi_xe: schemas.Doi_xe_Create ):
    db_doi_xe = models.Doi_xe(**doi_xe.dict())
    db.add(db_doi_xe)
    db.commit()
    db.refresh(db_doi_xe)
    return db_doi_xe

def update_doi_xe(db: Session, id:int , doi_xe: schemas.Doi_xe_Create):
    db_doi_xe=get_doi_xe(db=db, id=id)
    db_doi_xe.ten_doi_xe=doi_xe.ten_doi_xe
    db.commit()
    db.refresh(db_doi_xe)
    return db_doi_xe

def delete_doi_xe (db: Session , id:int):
        db_doi_xe = get_doi_xe(db=db , id=id)
        db.delete(db_doi_xe)
        db.commit()

#crud cho xe
def get_xe(db: Session, id:int):
    return db.query(models.Xe).filter(models.Xe.id == id).first()

def get_all_xe(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Xe).offset(skip).limit(limit).all()

"""
#take this as hint to write crud for create_xe
def create_user_groups(db: Session, user_groups: schemas.UserGroupsBase):
    db_user = db.query(models.User).filter(models.User.id == user_groups.id_user).first()
    db_group = db.query(models.Group).filter(models.Group.id == user_groups.id_group).first()

    if not db_user and db_group:
        raise HTTPException(status_code=409, detail="User or Group not found in system.")

    db_user.groups.append(db_group)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
"""

#endpoint input cho xe va tai xe association table
def create_xetaixe(db:Session , xetaixe : schemas.Xe_taixe):
    db_xe=db.query(models.Xe).filter(models.Xe.id==xetaixe.xe_id).first()
    db_taixe=db.query(models.Tai_xe).filter(models.Tai_xe.id==xetaixe.taixe_id).first()
    db_xe.xe_tai_xe.append(db_taixe)
    db.add(db_xe)
    db.commit()
    return "ok"
###############################################################################

def create_xe(db:Session,  xe : schemas.Xe_Create ):
    #db_xe = models.Xe( **xe.dict())
    db_xe = models.Xe(ten_xe=xe.ten_xe, doi_xe_id=xe.doi_xe_id)
    if len(xe.tai_xe_id):
        taixe = db.query(models.Tai_xe).filter(models.Tai_xe.id.in_(xe.tai_xe_id))#.first()
        for tungtaixe in taixe:
            db_xe.xe_tai_xe.append(tungtaixe)

    db.add(db_xe)
    db.commit()
    db.refresh(db_xe)
    return db_xe
#
def update_xe(db:Session, xe: schemas.Xe_Base,id :int):
    db_xe=get_xe(db=db, id=id)
    db_xe.ten_xe = xe.ten_xe
    db_xe.doi_xe_id = xe.doi_xe_id
    db.commit()
    db.refresh(db_xe)
    return db_xe

def delete_xe (db:Session , id:int):

    db_xe = get_xe(db=db , id=id)
    db.delete(db_xe)
    db.commit()


#Crud cho tai xe
def get_tai_xe(db:Session, id:int):
    return db.query(models.Tai_xe).filter(models.Tai_xe.id == id).first()

def get_all_tai_xe(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tai_xe).offset(skip).limit(limit).all()

#https://stackoverflow.com/questions/41270319/how-do-i-query-an-association-table-in-sqlalchemy hint to write following query
def get_chuyenxe_theo_tai_xe(db: Session, id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Tai_xe,models.Chuyen_xe,models.association_table_taixe_chuyenxe).filter(models.association_table_taixe_chuyenxe.c.tai_xe_id== models.Tai_xe.id).filter(models.association_table_taixe_chuyenxe.c.chuyen_xe_id == models.Chuyen_xe.id).filter(models.Tai_xe.id==id).all()

def create_tai_xe(db:Session, tai_xe: schemas.Tai_xe_Create):
    db_tai_xe = models.Tai_xe(ten_tai_xe= tai_xe.ten_tai_xe)

    if len(tai_xe.xe_id):
        xe = db.query(models.Xe).filter(models.Xe.id.in_(tai_xe.xe_id))#.first()
        for tungxe in xe:
            db_tai_xe.tai_xe_xe.append(tungxe)
    
    if len(tai_xe.chuyen_xe_id):
        chuyenxe = db.query(models.Chuyen_xe).filter(models.Chuyen_xe.id.in_(tai_xe.chuyen_xe_id))#.first()
        for tungchuyenxe in chuyenxe:
            db_tai_xe.tai_xe_chuyen_xe.append(tungchuyenxe)

    db.add(db_tai_xe)
    db.commit()
    db.refresh(db_tai_xe)
    return db_tai_xe

def update_tai_xe(db:Session, id:int , tai_xe : schemas.Tai_xe_Base ):
    db_tai_xe=get_tai_xe(db=db, id=id)
    db_tai_xe.ten_tai_xe = tai_xe.ten_tai_xe
    db.commit()
    db.refresh(db_tai_xe)
    return db_tai_xe

def delete_tai_xe (db:Session , id:int):

    db_tai_xe = get_tai_xe(db=db , id=id)
    db.delete(db_tai_xe)
    db.commit()

#crud cho chuyen xe
def get_chuyen_xe(db:Session, id:int):
    return db.query(models.Chuyen_xe).filter(models.Chuyen_xe.id == id).first()

def get_all_chuyen_xe(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Chuyen_xe).offset(skip).limit(limit).all()



def create_chuyen_xe(db:Session, chuyen_xe: schemas.Chuyen_xe_Create):
    db_chuyen_xe = models.Chuyen_xe(ten_chuyen_xe=chuyen_xe.ten_chuyen_xe)

    if len(chuyen_xe.tai_xe_id):
        taixe = db.query(models.Tai_xe).filter(models.Tai_xe.id.in_(chuyen_xe.tai_xe_id))#.first()
        for tungtaixe in taixe:
            db_chuyen_xe.chuyen_xe_tai_xe.append(tungtaixe)

    db.add(db_chuyen_xe)
    db.commit()
    db.refresh(db_chuyen_xe)
    return db_chuyen_xe

def update_chuyen_xe(db:Session, id:int , chuyenxe : schemas.Chuyen_xe_Base ):
    db_chuyen_xe=get_chuyen_xe(db=db, id=id)
    db_chuyen_xe.ten_chuyen_xe = chuyenxe.ten_chuyen_xe
    db.commit()
    db.refresh(db_chuyen_xe)
    return db_chuyen_xe

def delete_chuyen_xe (db:Session , id:int):
    db_chuyen_xe = get_chuyen_xe(db=db , id=id)
    db.delete(db_chuyen_xe)
    db.commit()