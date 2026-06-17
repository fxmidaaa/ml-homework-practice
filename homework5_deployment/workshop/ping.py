from fastapi import FastAPI

app = FastAPI(title='ping')

@app.get('/ping')
def ping():
    return 'pong'