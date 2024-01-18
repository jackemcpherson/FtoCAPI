from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class ConvertRequest(BaseModel):
    units: str
    value: float


def celsius_to_fahrenheit(celsius: float) -> float:
    return (9 / 5) * celsius + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (5 / 9) * (fahrenheit - 32)


@app.post("/convert/")
def convert(request: ConvertRequest = Body(...)):  # Add Body annotation here
    input_units = request.units
    if input_units == "celsius":
        fahrenheit = celsius_to_fahrenheit(request.value)
        return {"units": "fahrenheit", "value": fahrenheit}
    elif input_units == "fahrenheit":
        celsius = fahrenheit_to_celsius(request.value)
        return {"units": "celsius", "value": celsius}
