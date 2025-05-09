from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 

# create an app instance
app = FastAPI(
    title = "Insurance application"
)

# define the root endpoint.
@app.get("/")
def root():
    return {"message": "we are live!!"}

# an endpoint that greets people
@app.post("/greet/")
def greet(name: str, year_birth: int):
    age = 2025 - year_birth
    return {
        "greeting": f"Hi {name} how are you?",
        "age": f"Wow, you are {age} years old"
    }



if __name__ == "__main__":
    uvicorn.run("main:app", port = 8000, host = "localhost", reload = True)

