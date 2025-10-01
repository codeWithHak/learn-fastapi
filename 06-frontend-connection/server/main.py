from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # what id this CORSMiddleware? 
import uvicorn

app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(

    #* CORSMiddleware Explanation:
    # Browsers are very suspicious if your frontend is running at localhost:3000 adn it tries to call your backend at localhost:8000
    # The browser says:
    # Wait a sec, these are different origins (ports differ), maybe it’s a hacker trick

    # That’s a CORS (Cross-Origin Resource Sharing) issue.
    # CORSMiddleware is like a bouncer at the backend door, saying:
    # “Don’t worry browser, localhost:3000 is a friend, let them in.”

    CORSMiddleware,
    allow_origins=origins, # Who is allowed to talk to your backend.
    allow_credentials=True, # This is for cookies, authorization headers, or authentication tokens.
    allow_methods=["*"], # What HTTP methods are allowed?
    allow_headers=["*"], # What request headers can the frontend send?
)

@app.get("/hello")
async def hello(): # Why async?
    return "Hello"

@app.get("/bye")
async def bye(): # Why async?
    return "Bye"

# what is curl?
# and who we are calling?
# curl http://127.0.0.1:8000/hello
# -> {"message":"Hello from FastAPI"}

# Curl and postman are the same?

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)