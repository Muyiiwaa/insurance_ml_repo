from pydantic import BaseModel,Field
from typing import Literal


# define the request object
class EmailRequest(BaseModel):
    email_content: str = Field(...,
                               description="The email content to be checked",
                               examples=["Hi John, have you seen the movie ?"])

# define the response object
class EmailResponse(BaseModel):
    email_class: Literal['Real Email', 'Spam Email'] = Field(..., 
                                                      examples=["Real Email"],
                                                      description="the model predicted class.")
    probability: float = Field(..., description="The probability of evidence supporting the model decision",
                               ge=0, le=1, examples=[0.8553])

