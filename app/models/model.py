from core.setup import  Model, Column, String, Integer, ForeignKey


class User(Model):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    surname = Column(String())
    age = Column(Integer())


class Book(Model):
    __tablename__ = 'book'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    author = Column(String())
    price = Column(Integer())
    user_id = Column(Integer(), ForeignKey('user.id', ondelete="CASCADE"))



