from pydantic                   import BaseModel
        
class Admin (BaseModel):
    email                   :   str
    isblocked               :   bool
    name                    :   str
    surname                 :   str
    class Config:
        orm_mode = True        
