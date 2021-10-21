import  uvicorn
import  os
import  crud
from    fastapi                 import FastAPI, Depends, HTTPException
from    fastapi.middleware.cors import CORSMiddleware
from    db                      import SessionLocal
from    schema                  import Admin       
                                
app = FastAPI()
app.add_middleware( CORSMiddleware, 
                    allow_origins=["*"], 
                    allow_credentials=True, 
                    allow_methods=["*"],
                    allow_headers=["*"],
                    )

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/admins/{id}')
def get_admin_by_id (id:int, db=Depends(db)):
    admin = crud.get_admin_by_id(db, id)
    if admin:
        return admin
    else:
        raise HTTPException(404, crud.error_message(f'el administrador con id: {id} no existe'))
                    
@app.get('/admins/email/{email}')
def get_admin_by_email (email:str, db=Depends(db)):
    admin = crud.get_admin_by_email(db, email)
    if admin:
        return admin
    else:
        raise HTTPException(404, crud.error_message(f'el administrador con email: {email} no existe'))

@app.get('/admins/all/')
def get_admins (db=Depends(db)):
    admins = crud.get_admins(db)
    if admins:
        return admins
    else:
        raise HTTPException(404, crud.error_message(f'No existen administradores'))

@app.post('/admins/')
def create_admin(admin: Admin, db=Depends(db)):
    admin_exist = crud.get_admin_by_email(db, admin.email)
    if admin_exist:
        raise HTTPException(404, detail= crud.error_message(f'el administrador con email: {admin.email} ya existe'))
    return crud.create_admin(db, admin)

@app.put('/admins/')
def update_admin(id: int , admin: Admin, db=Depends(db)):
    admin_exist = crud.get_admin_by_id(db, id)
    if admin_exist is None:
        raise HTTPException(404, detail= crud.error_message(f'el administrador con id: {id} no existe'))
    return crud.update_admin(db, id, admin)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=int(os.environ.get('PORT')), reload=True)        
