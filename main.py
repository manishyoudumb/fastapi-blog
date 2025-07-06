from fastapi import FastAPI 

app = FastAPI(
    title="Blog API",
    description="Blog API with FastAPI",
    version="0.0.1"
)

@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}