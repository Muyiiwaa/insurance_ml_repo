from fastapi import FastAPI
import uvicorn
from schema import RootResponse



# initialize an app instance
app = FastAPI(
    title= "Appclick Restaurant Endpoints",
    summary= "This app contains all the endpoints for appclick restaurant",
    version= "v1"
)

@app.get('/',response_model=RootResponse)
async def root():
    """
    This is the root endpoint that serves as the app homepage.
    It does not require any parameter to function.
    """
    return RootResponse(
        message= "Appclick Restaurant is live!"
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",port=8000,reload=True)

