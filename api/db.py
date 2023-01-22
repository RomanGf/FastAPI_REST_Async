from sqlalchemy import (
    Column, 
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)

from databases import Database

DATABASE_URL = 'mysql://root:@localhost/articledb'

engine = create_engine(DATABASE_URL)

metadata = MetaData() 

Article = Table(
    'article',
    metadata,
    Column('id', Integer, primary_key= True),
    Column('title', String(200)),
    Column('description', String(400)),
)

User = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key= True),
    Column('username', String(20)),
    Column('password', String(200000000)),
)

database = Database(DATABASE_URL)