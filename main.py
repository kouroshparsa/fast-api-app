from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
# from app.controllers import api_controller
# from sqlalchemy.orm import Session
# from app.data_transfer_objects import UpdateCustomer
# from app.database import SessionLocal, engine
# from app.models import model
# model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.get('/api/payment/{id}')
# async def get_payment(id: int, db: Session = Depends(get_db)):
#     res = api_controller.get_payment(db, id)
#     if res is None:
#         return JSONResponse("Invalid payment_id", status_code=status.HTTP_404_NOT_FOUND)
#     return res
#
#
# @app.post('/api/customer/')
# async def update_customer(data: UpdateCustomer, db: Session = Depends(get_db)):
#     api_controller.set_customer_status(db, data.email, data.active)

@app.get('/test')
async def test():
    return JSONResponse({'name': 'kourosh'})