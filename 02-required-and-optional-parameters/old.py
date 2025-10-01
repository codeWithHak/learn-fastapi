from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Simple Text API",
    description="A simple API for text processing",
    version="0.116.0"
)

# a pydantic model for request
class TextRequest(BaseModel):
    text:str
    uppercase:Optional[bool] = False

# a pydantic model for request
class TextResponse(BaseModel):
    processed_text: str
    length: int


# define a route
@app.get("/")
def read_route() -> dict:
    return {"message":"hellp basic text api"}


# define a POST endpoint for text processing
@app.post("/process-text", response_model=TextResponse)
def process_text(request:TextRequest):
    text = request.text

    # if text is empty raise an HTTPException    
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    # text will be stored in uppercase in processed_text varaible if user set uppercase True in request
    # else simple text will be stored in processed_text variable.
    processed_text = text.upper() if request.uppercase else text

    # create response using pydantic model
    response = TextResponse(
        processed_text=processed_text,
        length=len(processed_text)
    )

    return response


if __name__ == "__main__":
    uvicorn.run(app="old:app", reload=True)
