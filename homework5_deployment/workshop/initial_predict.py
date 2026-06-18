import pickle
from fastapi import FastAPI
import uvicorn
from typing import Literal
from pydantic import BaseModel, Field

class Customer(BaseModel):
    gender: Literal['male', 'female']
    seniorcitizen: Literal[0, 1]
    partner: Literal['yes', 'no']
    dependents: Literal['yes', 'no']
    phoneservice: Literal['yes', 'no']
    multiplelines: Literal['no', 'yes', 'no_phone_service']
    internetservice: Literal['fiber_optic', 'dsl', 'no']
    onlinesecurity: Literal['no', 'yes', 'no_internet_service']
    onlinebackup: Literal['no', 'yes', 'no_internet_service']
    deviceprotection: Literal['no', 'yes', 'no_internet_service']
    techsupport: Literal['no', 'yes', 'no_internet_service']
    streamingtv: Literal['no', 'yes', 'no_internet_service']
    streamingmovies: Literal['no', 'yes', 'no_internet_service']
    contract: Literal['month-to-month', 'one_year', 'two_year']
    paperlessbilling: Literal['yes', 'no']
    paymentmethod: Literal[
        'electronic_check', 
        'mailed_check', 
        'bank_transfer_(automatic)', 
        'credit_card_(automatic)'
    ]

    tenure: int = Field(..., ge=0)
    monthlycharges: float = Field(..., ge=18.25)
    totalcharges: float = Field(..., ge=0.0)


class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool


app = FastAPI(title='churn-prediction')

model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)

def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)

@app.post('/predict')
def predict(customer: Customer) -> PredictResponse:
    prob = predict_single(customer.model_dump())
    return PredictResponse(
        churn_probability = prob,
        churn= bool(prob >= 0.5)
    )

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9696)

# customer = {
#     'gender': 'female',
#     'seniorcitizen': 0,
#     'partner': 'yes',
#     'dependents': 'no',
#     'phoneservice': 'no',
#     'multiplelines': 'no_phone_service',
#     'internetservice': 'dsl',
#     'onlinesecurity': 'no',
#     'onlinebackup': 'yes',
#     'deviceprotection': 'no',
#     'techsupport': 'no',
#     'streamingtv': 'no',
#     'streamingmovies': 'no',
#     'contract': 'month-to-month',
#     'paperlessbilling': 'yes',
#     'paymentmethod': 'electronic_check',
#     'tenure': 1,
#     'monthlycharges': 29.85,
#     'totalcharges': 29.85
# }

# X = dv.transform([customer])
# y_pred = model.predict_proba(X)[0, 1]

# print('input', customer)
# print('churn probability:', y_pred)