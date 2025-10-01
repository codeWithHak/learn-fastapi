from fastapi import FastAPI, HTTPException
from validations import TextRequest, TextResponse
import uvicorn


app = FastAPI(title="Text Processing",description="A text procesing Fast API App")

@app.get("/")
def read_route():
    return{"message": "Welcome to our Text Processing App"}

@app.post("/process_text", response_model=TextResponse)
def process_text(request:TextRequest) -> TextResponse:
    text:str = request.text

    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    processed_text:str = text.upper() if request.uppercase else text

    result:TextResponse =  TextResponse(
        processed_text=processed_text,
        text_length=len(processed_text)
    )

    return result

# an example of path parameter below you can easily get the response on:http://127.0.0.1:8000/users/huzair
# path parameters are used for obviuos routes 
# 
 
"""@app.get("/users/{user_name}")
def get_users(user_name:str):
    return {"message":f"Welcome {user_name}"}


@app.get("/books")
def get_books(category:str, books_available:int):
    return {"message":f"{books_available} books are available in category {category}"}
"""

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)