from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_route():
    return {
        "message":"Hello and welcome :)"
    }

@app.get("/books")
def get_books():
    return[
        {"book_1":"Atomic Habits"},
        {"book_2":"Power Of Manifestation"},
        {"book_3":"The Law Of Attraction"},
    ]

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)