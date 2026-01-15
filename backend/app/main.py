from fastapi import FastAPI

app = FastAPI(title="Prototype")


@app.get("/")
def root():
    return {"status": "ok"}
