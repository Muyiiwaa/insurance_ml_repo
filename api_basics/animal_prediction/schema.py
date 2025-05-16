from pydantic import BaseModel, Field
from typing import Literal


# define the model response
class UserResponse(BaseModel):
    predicted_class: Literal['bear','horse','kangaroo','0wl','whale'] = Field(..., description="The predicted animal class",examples=["owl"])
    probability: float = Field(..., description="The probability associated with the predicted class", examples=[0.69], ge=0, le=1)