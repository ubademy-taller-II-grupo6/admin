from db                  import Base
from sqlalchemy          import Column, Integer, String, Boolean

class Admin(Base):
    __tablename__   = 'admins'
    id              = Column(Integer, primary_key = True)
    email           = Column(String)
    isblocked       = Column(Boolean)
    name            = Column(String)
    surname         = Column(String)
    