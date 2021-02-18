from typing import Any, Dict, List
from pydantic import BaseModel


class UserSchema(BaseModel):

    name: str
    surname: str
    age: int

    class Config:
        schema_extra = {
            "example":{
                "name": "My name",
                "surname": "My surname",
                "age": 0
            }
        }
        orm_mode = True


class Alluser(BaseModel):
    data: List[UserSchema] = None

    class Config:
        orm_mode = True

class UpdateUserSchema(BaseModel):

    name: str = ""
    surname: str = ""
    age: int


    class Config:
        schema_extra = {
            "example":{
                "name": "New name",
                "surname": "New surname",
                "age": 0
            }
        }
        orm_mode = True

class BookSchema(BaseModel):

    title: str
    author: str
    price: int

    class Config:
        schema_extra = {
            "example" :{
                "title": "Book title",
                "author": "Book author",
                "price": 0
            }
        }
        orm_mode = True


class Allbook(BaseModel):

    book_data: List[BookSchema] = None
    user: Dict[str,Any] =None
    class Config:
        orm_mode = True

class Onebook(BaseModel):
    user: Dict[str, Any] = None
    book_data: BookSchema = None

    class Config:
        exclude = {'user_id'}
        # fields = {
        #     'book_data':{
        #         'exclude':'user_id'
        #     }
        # }
        orm_mode = True

class UpdateBookSchema(BaseModel):

    title: str = ""
    author: str = ""
    price: int

    class Config:
        schema_extra = {
            "example": {
                "title": "New title",
                "author": "New author",
                "price": 0
            }
        }
        orm_mode = True


class Response404(BaseModel):

    status_code: int
    content: dict

    class Config:
        schema_extra = {
            "example":{
                "status_code" : 404,
                "content": {"result":False}
            }
        }

