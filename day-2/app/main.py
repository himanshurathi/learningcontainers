from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello from multi-stage Python build!"}

@app.get("/health")
def health():
    return {"status": "ok"}
