from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
import models, schemas , crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI(title='FastAPI + SQL server CRUD')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/users/' , response_model=schemas.UserResponse)
def create_user(user : schemas.UserCreate , db : Session = Depends(get_db)):
    return crud.create_user(db ,user)

@app.get('/users/')
def read_users(db : Session = Depends(get_db)):
    return crud.get_users(db)

@app.get('/users/{user_id}')
def read_user( user_id : int ,db : Session =Depends(get_db)):
    user = crud.get_user(db , user_id)
    if not user:
        raise HTTPException(status_code=404 , detail='user not found')
    return user

@app.put('/users/{user_id}')
def update_user(user_id : int , user: schemas.UserUpdate , db :Session = Depends(get_db)):
    updated =crud.update_user(db, user_id , user)
    if not updated:
        raise HTTPException(status_code=404 , detail='user not found')
    return updated

@app.delete('/users/{user_id}')
def delete_user(user_id : int , db : Session =Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail='user not found')
    return {'message' : 'user deleted successfully'}