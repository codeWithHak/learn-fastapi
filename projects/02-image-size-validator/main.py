from typing import Annotated

from fastapi import FastAPI, File

import uvicorn

app = FastAPI()

@app.get("/")
async def read_route():
    return "Hello"


@app.post("/files/")

# we set the type of data to File(...) which means now fatapi will expect a file (multipart/formdata), by default it expects a string.

async def create_file(file:bytes = File(...)):
    length = len(file) / (1024 * 1024)
    
    message = "Valid file" if length <= 2  else "File is too large"
    response = {
        "message":message,
        "length": f"{length:.2f} mb"
    }
    return response

if __name__ == "__main__":
    uvicorn.run(app="test:app", host="127.0.0.1" ,port=800, reload=True)