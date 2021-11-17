from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from server.database.models.user import User
from server.database.connection import db
from server.assets.schemas import user

router = APIRouter()

fake_data = dict(
    user_id='test',
    password='ljsdfoqwer',
    nickname='gildongstar',
    name='honggildong',
    email='gildong@gmail.com',
    phone='010-123-4567'
)

fake2_data = dict(
    user_id='kimcheolsu',
    password='cheolsu123',
    nickname='cheolsuhaja',
    name='kimcheolsu',
    email='cheolsu@gmail.com',
    phone='010-321-7654'
)

@router.get('/users')
async def get_user(
    id: int,
) -> JSONResponse:
    user = User.find(id)
    if user:
        return JSONResponse(status_code=200, content=jsonable_encoder({'user': user}))
    else:
        return JSONResponse(status_code=404, content=jsonable_encoder({'user': 'not found'}))
    
@router.post('/users')
async def create_user(
    user: user.CreateUser
) -> JSONResponse:
    new_user = User.create(**user.dict(), auto_commit=True)
    
    return JSONResponse(status_code=200, content=jsonable_encoder({'user': new_user}))

@router.delete('/users')
async def delete_user(
    id: str
) -> JSONResponse:
    user = User.find(id)
    try:
        user.delete()
    except:
        return JSONResponse(status_code=404, content=jsonable_encoder({'error': 'user not found'}))
    
    return JSONResponse(status_code=200, content=jsonable_encoder({'success': 'OK'}))

@router.put('/users')
async def update_user(
    id: int,
    user: user.UpdateUser
) -> JSONResponse:
    update_user = User.find(id)
    if not update_user:
        return JSONResponse(status_code=404, content=jsonable_encoder({'error': 'user not found'}))
    new_user = update_user.update(**user.dict())
    
    return JSONResponse(status_code=200, content=jsonable_encoder({'user': new_user}))