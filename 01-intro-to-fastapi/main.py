from fastapi import FastAPI
import uvicorn

app = FastAPI(
    description="Basic FastAPI",
    version="0.116.0"
)

@app.get("/")
def home() -> dict:
    return {"message":"Hello from fastapi"}

@app.get("/hello/{name}")
def read_user(name:str) -> dict:
    return {"message": f"Hello {name}" }


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
