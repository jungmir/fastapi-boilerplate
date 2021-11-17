from typing import Optional
from pydantic import BaseModel

class CreateUser(BaseModel):
    user_id: str
    password: str
    nickname: str
    name: str
    email: str
    phone: str
    
    class Config:
        schema_extra = {
            "example": {
                "user_id": "gildong23",
                "password": "alsjdfqwiusglasdf",
                "nickname": "gildongangel",
                "name": "honggildong",
                "email": "gildong23@gmail.com",
                "phone": "010-345-7423"
            }
        }
        
class UpdateUser(CreateUser):
    class Conifg:
        schema_extra = {
            "example": {
                "user_id": "gildong23",
                "password": "alsjdfqwiusglasdf",
                "nickname": "gildongangel",
                "name": "honggildong",
                "email": "gildong23@gmail.com",
                "phone": "010-345-7423"
            }
        }
    
class ModifyUser(BaseModel):
    user_id: Optional[str]
    password: Optional[str]
    nickname: Optional[str]
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    
    class Conifg:
        schema_extra = {
            "example": {
                "user_id": "gildong23",
                "password": "alsjdfqwiusglasdf",
                "nickname": "gildongangel",
                "name": "honggildong",
                "email": "gildong23@gmail.com",
                "phone": "010-345-7423"
            }
        }