from tasks import helo_world
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    helo_world.delay()
    helo_world()
    return {"message":"SUCCESS"}
