from typing import List, Union

from pydantic import BaseModel

class Doi_xe_Base(BaseModel):
    
    ten_doi_xe: str


class Doi_xe_Create(Doi_xe_Base):
    pass


class Doi_xe(Doi_xe_Base):
    id: int
    class Config:
        orm_mode = True


class Xe_Base(BaseModel):
    ten_xe: str
    doi_xe_id: int



class Xe_Create(Xe_Base):
    
    tai_xe_id : List[int] = []
    #tai_xe_id : int


class Xe(Xe_Base):
    id: int
    xe_tai_xe: List['Tai_xe'] =[]

    class Config:
        orm_mode = True


class Tai_xe_Base(BaseModel):
    ten_tai_xe: str
    

class Tai_xe_Create(Tai_xe_Base):
    pass
    #chuyen_xe_id: List[int] =[]

class Tai_xe(Tai_xe_Base):
    id: int
    tai_xe_chuyen_xe: List['Chuyen_xe'] = []
   

    class Config:
        orm_mode = True

class Chuyen_xe_Base(BaseModel):
    ten_chuyen_xe: str


class Chuyen_xe_Create(Chuyen_xe_Base):
    pass


class Chuyen_xe(Chuyen_xe_Base):
    id: int

    class Config:
        orm_mode = True
