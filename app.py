from tasks import helo_world
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    hello = helo_world.delay()
    return {"message":"SUCCESS"}
