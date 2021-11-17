from sqlalchemy import Column, Integer, String, ForeignKey, Text
from server.database.models.mixin.base import BaseMixin

class User(BaseMixin):
    __tablename__ = 'users'
    __repr_attrs__ = ['user']
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, unique=True, index=True)
    password = Column(String)
    nickname = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
    
    class Config:
        orm_mode = True