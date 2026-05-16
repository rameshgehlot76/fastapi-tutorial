from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    name: str
    age: int
    height: float
    weight: float

@app.post("/predict")
def predict(data: InputData):
    return {"message": f"Hello {data.name}, age {data.age}"}

