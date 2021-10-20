from    sqlalchemy.orm  import Session
import  schema, models

def get_admin_by_id(db: Session, id: int = None):
    if id:
        return db.query (models.Admin).filter(models.Admin.id == id).first()

def get_admin_by_email(db: Session, email: str = None):
    if email:
        return db.query (models.Admin).filter(models.Admin.email == email).first()
    
def get_admins(db: Session):
    return db.query (models.Admin).all()
        
def create_admin(db: Session, admin: schema.Admin):
    admin_model  = models.Admin(**admin.dict())
    db.add(admin_model)
    db.commit()
    db.refresh(admin_model)
    return admin_model

def update_admin(db: Session, id: int, admin: schema.Admin):
    admin_model                 = models.Admin(**admin.dict())
    admin_to_update             = db.query (models.Admin).filter(models.Admin.id == id).first() 
    admin_to_update.email       = admin_model.email
    admin_to_update.isblocked   = admin_model.isblocked
    admin_to_update.name        = admin_model.name 
    admin_to_update.surname     = admin_model.surname
    db.add(admin_to_update)
    db.commit()
    db.refresh(admin_to_update)
    return admin_to_update

def error_message(message):
    return {
        'error': message
    }
