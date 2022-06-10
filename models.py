from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class Doi_xe(Base):
    __tablename__="doi_xe"
    id = Column(Integer, primary_key=True)
    ten_doi_xe = Column(String(80))
    #doi xe lien ket 1 to many voi xe
    xe_id = relationship("Xe", back_populates="doi_xe")

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
    doi_xe_id = Column( Integer, ForeignKey("doi_xe.id"))    

    doi_xe = relationship( "Doi_xe" , back_populates="xe_id")    
    
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #tai_xe_xe = relationship( "Xe" , back_populates ="xe_tai_xe")

   
=======
    
    
>>>>>>> 60650329d9a79dfcba3bcbde0a8e93142c19981f
=======
    
    
>>>>>>> 60650329d9a79dfcba3bcbde0a8e93142c19981f
=======
    
    
>>>>>>> 60650329d9a79dfcba3bcbde0a8e93142c19981f
    #lien ket voi chuyen xe theo many to many

    tai_xe_chuyen_xe = relationship( "Chuyen_xe" , secondary= association_table_taixe_chuyenxe , backref="tai_xe" )


class Chuyen_xe(Base):
    __tablename__ = 'chuyen_xe'
    id = Column(Integer, primary_key=True)
    ten_chuyen_xe=Column(Text)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #chuyen_xe_tai_xe = relationship( "Tai_xe" , back_populates ="tai_xe_chuyen_xe")
=======
    
>>>>>>> 60650329d9a79dfcba3bcbde0a8e93142c19981f
=======
    
>>>>>>> 60650329d9a79dfcba3bcbde0a8e93142c19981f
=======
    
>>>>>>> 60650329d9a79dfcba3bcbde0a8e93142c19981f


    