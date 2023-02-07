from fastapi import FastAPI
from router import item

app = FastAPI()
app.include_router(item.router)

@app.get('/')
def root():
    return {"msg": "welcome to my world"}