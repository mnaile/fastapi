from fastapi import APIRouter, Path
from starlette.responses import JSONResponse
from app.models.model import User, Book
from app.schema.schema import UpdateBookSchema, UpdateUserSchema, UserSchema, BookSchema, Response404, Alluser, Allbook, Onebook
from app.helpers.helpers import create_user, read_all_users, read_one_user, updated_user, delete_user, created_book, read_all_book, read_one_book, updated_users_book, deleted_users_book


api = APIRouter()
    


# ======== CREATE USER =========


@api.post("/user", 
status_code=200,
tags=["Users"],
summary="Create User",
description="User description",
response_model=UserSchema,
responses={"404":{"model":Response404}})

async def created_user(user: UserSchema):

    return await create_user(user)
  
# ========== GET ALL USERS ==========


@api.get("/users",
status_code=200,
tags=["Users"],
summary="Get all users",
description="User description",
response_model=Alluser,
responses={"404":{"model":Response404}})

async def get_all_users():
    return await read_all_users()
    

# ============ GET ONE USER ===============


@api.get("/user/{id}",
status_code=200,
tags=["Users"],
summary="Get one user",
description="User description",
response_model=UserSchema,
responses={"404":{"model":Response404}})

async def get_one_user(id:int = Path(...)):
    return await read_one_user(id)


# ============== UPDATE USER DATA ==============


@api.put("/user/{id}",
status_code=200,
tags=["Users"],
summary="Update user info",
description="User description",
response_model=UpdateUserSchema,
responses={"404":{"model":Response404}})
async def update_user(user: UpdateUserSchema, id:int = Path(...)):
    return await updated_user(user, id)


# ============= DELETED USER FROM DB ============


@api.delete("/user/{id}",
status_code=200,
tags=["Users"],
summary="Deleted user from db",
description="User description",
responses={"404":{"model":Response404}})
async def deleted_user(id: int = Path(...)):
    return await delete_user(id)



# =============== CREATE BOOK FOR USER =============


@api.post("/user/{id}/book",
status_code=200,
tags=["Books"],
summary="Create book",
description="Book description",
response_model=BookSchema,
responses={"404":{"model":Response404}})
async def create_book(book: BookSchema, id:int=Path(...)):
    return await created_book(book, id)


# ================= GET USERS ALL BOOK ============


@api.get("/user/{id}/books",
status_code=200,
tags=["Books"],
summary="Get users all book",
description="Book description",
response_model=Allbook,
responses={"404":{"model":Response404}})
async def get_all_book(id:int = Path(...)):
    return await read_all_book(id)


# ============= GET USERS ONE BOOK ============


@api.get("/user/{user_id}/book/{id}",
status_code=200,
tags=["Books"],
summary="Get uses one book",
description="Book description",
response_model=Onebook,
responses={"404":{"model":Response404}})
async def get_one_book(user_id: int = Path(...), id: int = Path(...)):
    return await read_one_book(user_id, id)


# =============== UPDATE USERS BOOK =============


@api.put("/user/{user_id}/book/{id}",
status_code=200,
tags=["Books"],
summary="Update users book",
description="Book description",
response_model=UpdateBookSchema,
responses={"404":{"model":Response404}})
async def update_book(book:UpdateBookSchema, user_id: int = Path(...), id: int = Path(...)):

    return await updated_users_book(book, user_id, id)

      
# ====================== DELETE BOOK ===============================


@api.delete("/user/{user_id}/book/{id}",
status_code=200,
tags=["Books"],
summary="Deleted book",
description="Book description",
responses={"404":{"model":Response404}})
async def deleted_book(user_id: int = Path(...), id: int = Path(...)):
    
    return await deleted_users_book(user_id, id)



