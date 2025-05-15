from fastapi import FastAPI
import uvicorn
from utils import get_artifacts, get_description, check_email
from schema import EmailRequest, EmailResponse
import logfire


# create an app instance
app = FastAPI(
    title= "Email Classifier Application",
    description= get_description(),
    version="V1"
)
 # init logfire monitoring
logfire.configure(token = "TOKEN GOES HERE")
logfire.instrument_fastapi(app)

# create the root endpoint
@app.get("/")
async def root():
    return {"message":"We are up and healthy!"}

@app.post("/predict/", response_model=EmailResponse)
def predict_email(email_payload: EmailRequest):
    """_This endpoint accepts a json payload containing the 
    email content as a post request and returns the class of email
    that the content belongs to with the associated probability._

    Args:
        email_payload (EmailRequest): _The json payload containing the email content._

    """
    email = email_payload.email_content
    email_class, probability = check_email(email_text=email)
    logfire.info(f"class:{email_class}, probaility: {probability}")
    return EmailResponse(
        email_class=email_class,
        probability=probability
    )

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, host="localhost",
                reload=True)