from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Define the Data Models
class CelsiusToFahrenheitRequest(BaseModel):
    celsius: float


class FahrenheitToCelsiusRequest(BaseModel):
    fahrenheit: float


# Processing Functions
def celsius_to_fahrenheit(celsius: float) -> float:
    return (9 / 5) * celsius + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (5 / 9) * (fahrenheit - 32)


# Define App Routes
@app.post("/convert/c_to_f")
def convert_c_to_f(request: CelsiusToFahrenheitRequest):
    fahrenheit = celsius_to_fahrenheit(request.celsius)
    return {"fahrenheit": fahrenheit}


@app.post("/convert/f_to_c")
def convert_f_to_c(request: FahrenheitToCelsiusRequest):
    celsius = fahrenheit_to_celsius(request.fahrenheit)
    return {"celsius": celsius}
