from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import re

app = FastAPI(
    title="Basic Email Validator",
    description="A basic email validator using FastAPI",
    version="0.116.0"
)

class EmailRequest(BaseModel):
    email:str


class EmailResponse(BaseModel):
    message:str


@app.get('/')
def read_route():
    return {"message":"Hello"}


@app.post("/validate-email",response_model=EmailResponse)
def validate_email(request:EmailRequest):

    email = request.email

    if not email:
        raise HTTPException(status_code=400, detail="email not provided")
    
    if re.search("@",email) and re.search(".com$",email):
        response = EmailResponse(message="Email Verified!")
        return response
    else:
        response = EmailResponse(message="Email Not Verified!")
        return response
    # message = "Your email is validated" if request.is_validation_enable else "Email recieved but not verified"

if __name__ == "__main__":
    uvicorn.run(app="main:app",port=800, host="127.0.0.1", reload=True)
    
