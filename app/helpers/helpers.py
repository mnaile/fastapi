from fastapi import Path
from starlette.responses import JSONResponse
from app.models.model import User, Book
from app.schema.schema import UpdateBookSchema, UpdateUserSchema, UserSchema, BookSchema, Response404, Alluser, Allbook, Onebook
from core.settings.app_factory import logger




async def clear_dict(schema):
    return {key: val for key, val in schema.dict().items() if val}


# ======== CREATE USER =========


async def create_user(user: UserSchema) -> UserSchema:
    try:
        user = await User.create(**user.dict())
        return UserSchema.from_orm(user)

    except Exception as err:
        print(err)
        return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())


  
# ========== GET ALL USERS ==========


async def read_all_users():
    try:
        user = await User.query.gino.all()

        logger.info("Get all users")
        return Alluser(data=user)

    except Exception as err:
        print(err)
        return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())


# ============ GET ONE USER ===============


async def read_one_user(id:int = Path(...)):
    try:

        user = await User.query.where(User.id == id).gino.first()
        if not user:
            logger.info("User not found")
            return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())
        return user

    except Exception as err:
        print(err)
        return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())


# ============== UPDATE USER DATA ==============


async def updated_user(user: UpdateUserSchema, id:int = Path(...)) -> UpdateUserSchema:

    try:        
        result = await User.query.where(User.id == id).gino.first()
        if not result:
            return JSONResponse(**Response404(status_code=404, content={"result": False}).dict())
        user = await clear_dict(user)
        await result.update(**user).apply()

        return result

    except Exception as err:
        return JSONResponse(**Response404(status_code=404, content={"result": False}).dict())



# ============= DELETED USER FROM DB ============


async def delete_user(id: int = Path(...)):
    try:
        user = await User.query.where(User.id == id).gino.first()
        if not user:
            return JSONResponse(**Response404(status_code=404, content={"result":False}))
        await user.delete()
        return {"result" : True}
    
    except Exception as err:
        return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())


# =============== CREATE BOOK FOR USER =============


async def created_book(book: BookSchema, id: int = Path(...)) -> BookSchema:
    try:

        user = await User.query.where(User.id == id).gino.first()
        if not user:
            return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())
        
        book = book.dict()
        book["user_id"] = user.id

        book = await Book.create(**book)

        return BookSchema.from_orm(book)
    
    except Exception as err:
        return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())


# ================= GET USERS ALL BOOK ============


async def read_all_book(id: int = Path(...)):
    try:
        user = await User.query.where(User.id==id).gino.first()
        if not user:
            return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())
        book = await Book.query.where(Book.user_id == id).gino.all()
        
        return Allbook(user=user.to_dict(),book_data=book)
    except Exception as err:
        return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())


# ============= GET USERS ONE BOOK ============


async def read_one_book(user_id: int = Path(...), id: int = Path(...)):
    try:
        user = await User.query.where(User.id == user_id).gino.first()
        if not user:
            return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())
        book = await Book.query.where(user_id==user_id and Book.id == id).gino.first()
        if not book:
            return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())

        return Onebook(user=user.to_dict(), book_data=BookSchema.from_orm(book))
    except Exception as err:
        return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())


# =============== UPDATE USERS BOOK =============


async def updated_users_book(book = UpdateBookSchema, user_id:int = Path(...), id:int = Path(...)) -> UpdateBookSchema :
    try:
        user = await User.query.where(User.id == user_id).gino.first()
        if not user:
            return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())
        result = await Book.query.where(user_id == user_id and Book.id == id).gino.first()
        if not result:
            return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())

        book = await clear_dict(book)
        await result.update(**book).apply()
        return result
    except Exception as err:
        return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())
        

# ====================== DELETE BOOK ===============================


async def deleted_users_book(user_id: int = Path(...), id:int = Path(...)):
    try:
        user = await User.query.where(User.id == user_id).gino.first()
        if not user:
            return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())
        book = await Book.query.where(user_id == user_id and Book.id == id).gino.first()
        if not book:
            return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())

        await book.delete()
        return {"result":True}
    except Exception as err:
        return JSONResponse(**Response404(status_code=404, content={"result":False}).dict())

