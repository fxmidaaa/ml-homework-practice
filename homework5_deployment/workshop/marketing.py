import requests

url = 'http://localhost:9696/predict'

customer = {
  "gender": "female",
  "seniorcitizen": 0,
  "partner": "yes",
  "dependents": "no",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 1,
  "monthlycharges": 29.85,
  "totalcharges": 29.85
}

response = requests.post(url, json=customer)
churn = response.json()

print('response: ', churn)

if churn['churn'] == True:
    print('send an email with promo!')
else:
    print('no promo')