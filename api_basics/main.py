from fastapi import FastAPI
import uvicorn
from schema import RootResponse,OrderRequest,OrderResponse
from utils import get_order,get_menu



# initialize an app instance
app = FastAPI(
    title= "Appclick Restaurant Endpoints",
    summary= "This app contains all the endpoints for appclick restaurant",
    version= "v1"
)

@app.get('/',response_model=RootResponse, tags=["Health"])
async def root():
    """
    This is the root endpoint that serves as the app homepage.
    It does not require any parameter to function.
    """
    return RootResponse(
        message= "Appclick Restaurant is live!"
    )


@app.post("/order/", response_model=OrderResponse, tags=["Restaurant"])
def get_orders(order: OrderRequest):
    """
    This endpoint accepts user order, process it and returns the
    total cost of their order. It expects the exact payload in the
    schema and returns a string object of the total cost.
    """
    user_order = order.model_dump()
    total_cost = get_order(**user_order)

    return OrderResponse(
        total_bill= f'${total_cost}'
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",port=8000,reload=True)

