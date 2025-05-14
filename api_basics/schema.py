from pydantic import BaseModel,Field


# create root response
class RootResponse(BaseModel):
    message: str = Field(..., examples=["Appclick Restaurant is live!"])

# create order request
class OrderRequest(BaseModel):
    rice: int = Field(..., description="The portion of rice",
                       examples=[0])
    beans: int = Field(..., description="The portion of beans",
                       examples=[0])
    beef: int = Field(..., description="The Number of beef",
                       examples=[0])
    chicken: int = Field(..., description="The Number of chicken",
                       examples=[0])

class OrderResponse(BaseModel):
    total_bill: str = Field(..., examples=["$0.0"])
