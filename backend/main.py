from fastapi import FastAPI
from routes.upload import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {
        "product": "Project Atlas",
        "version": "1.0.0",
        "status": "Running",
        "message": "Welcome to the Future of AI Decision Intelligence"
    }