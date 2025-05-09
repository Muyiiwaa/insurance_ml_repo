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

if __name__ == "__main__":
    uvicorn.run("main:app", port = 8000, host = "localhost", reload = True)

