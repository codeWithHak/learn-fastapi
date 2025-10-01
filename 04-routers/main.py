from fastapi import FastAPI
import uvicorn
from app_router import page_router  
app = FastAPI(title="Basic Router")


app.include_router(page_router)

@app.get("/")
def read_route():
    return {"message":"Welcome To Root"}


@app.get("/shop")
def shop():
    return {"message":"Welcome To Shop Page"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=600, reload=True)