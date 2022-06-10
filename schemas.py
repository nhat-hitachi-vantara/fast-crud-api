from typing import List, Union

from pydantic import BaseModel

class Doi_xe_Base(BaseModel):
    
    ten_doi_xe: str
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #xe_id: int
    #description: Union[str, None] = None
=======
=======
=======


class Doi_xe_Create(Doi_xe_Base):
    pass


class Doi_xe(Doi_xe_Base):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #id: int
=======
    id: int
=======
    id: int
=======
    id: int
    class Config:
        orm_mode = True


class Xe_Base(BaseModel):
    ten_xe: str
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    
=======
    
=======
    


class Xe_Create(Xe_Base):
    pass


class Xe(Xe_Base):
    id: int
    doi_xe_id: int
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #xe_tai_xe: int

=======
    xe_tai_xe: List['Tai_xe'] = []
=======
    xe_tai_xe: List['Tai_xe'] = []
=======
    xe_tai_xe: List['Tai_xe'] = []
    class Config:
        orm_mode = True


class Tai_xe_Base(BaseModel):
    ten_tai_xe: str
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
    
=======
    
=======
    

class Tai_xe_Create(Tai_xe_Base):
    pass


class Tai_xe(Tai_xe_Base):
    id: int
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #tai_xe_xe: int
    #tai_xe_chuyen_xe: int
=======
    tai_xe_chuyen_xe: List['Chuyen_xe'] = []
   
=======
    tai_xe_chuyen_xe: List['Chuyen_xe'] = []
   
=======
    tai_xe_chuyen_xe: List['Chuyen_xe'] = []
   

    class Config:
        orm_mode = True

class Chuyen_xe_Base(BaseModel):
    ten_chuyen_xe: str
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #description: Union[str, None] = None
=======
=======
=======


class Chuyen_xe_Create(Chuyen_xe_Base):
    pass


class Chuyen_xe(Chuyen_xe_Base):
    id: int
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #chuyen_xe_tai_xe: int
=======
=======
=======

    class Config:
        orm_mode = True
