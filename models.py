from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class Doi_xe(Base):
    __tablename__="doi_xe"
    id = Column(Integer, primary_key=True)
    ten_doi_xe = Column(String(80))
    #doi xe lien ket 1 to many voi xe
    #xe_id = relationship("Xe")

#bang associate cho xe va tai xe theo many to many
association_table_xetaixe = Table(

    "association table cho xe va tai xe",
    Base.metadata,
    Column("xe_id", ForeignKey("xe.id")),
    Column("tai_xe_id", ForeignKey("tai_xe.id")),
)

class Xe(Base):
    __tablename__ = 'xe'
    id = Column(Integer, primary_key=True)
    ten_xe = Column(Text)

    #lien ket voi doi xe 
    doi_xe_id = Column( Integer , default=0)    
    
    #doi xe lien ket many to many voi tai xe
    xe_tai_xe = relationship( "Tai_xe" , secondary = association_table_xetaixe , backref="xe")

association_table_taixe_chuyenxe = Table(
    "association table cho tai xe va chuyen xe",
    Base.metadata,
    Column("tai_xe_id", ForeignKey("tai_xe.id")),
    Column("chuyen_xe_id", ForeignKey("chuyen_xe.id")),
)

class Tai_xe(Base):
    __tablename__ = 'tai_xe'
    id = Column(Integer, primary_key=True)
    ten_tai_xe = Column(Text)
    #tai_xe_xe = relationship( "Xe" , back_populates ="xe_tai_xe")

   
    #lien ket voi chuyen xe theo many to many

    tai_xe_chuyen_xe = relationship( "Chuyen_xe" , secondary= association_table_taixe_chuyenxe , backref="tai_xe" )


class Chuyen_xe(Base):
    __tablename__ = 'chuyen_xe'
    id = Column(Integer, primary_key=True)
    ten_chuyen_xe=Column(Text)
    #chuyen_xe_tai_xe = relationship( "Tai_xe" , back_populates ="tai_xe_chuyen_xe")


    