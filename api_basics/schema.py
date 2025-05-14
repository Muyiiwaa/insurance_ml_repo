from pydantic import BaseModel,Field


# create root response
class RootResponse(BaseModel):
    message: str = Field(..., examples=["Appclick Restaurant is live!"])