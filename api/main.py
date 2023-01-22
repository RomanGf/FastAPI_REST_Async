from fastapi import FastAPI
from .db import metadata, database, engine, Article
from .articles import router as articles_router
from .users import router as users_router
from .auth import router as auth_router


metadata.create_all(engine)

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

app.include_router(articles_router)
app.include_router(users_router)
app.include_router(auth_router)