from pydantic import BaseModel

class UserSchema(BaseModel):
    title: str
    content: str
    like: int
    views: int
    
    class Config:
        schema_extra = {
            "example": {
                "title": "안녕하세요. html 개발자입니다.",
                "content": "미안하다.. 이거 보여주려고 어그로 끌었다.",
                "like": 2,
                "views": 123
            }
        }