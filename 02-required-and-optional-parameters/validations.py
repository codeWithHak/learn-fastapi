from pydantic import BaseModel

class TextRequest(BaseModel):
    text:str = ""
    uppercase:bool = False

class TextResponse(BaseModel):
    processed_text: str
    text_length:int
    

