from fastapi import FastAPI
from routes.upload import router

app = FastAPI()

# Register Upload APIs
app.include_router(router)

# Register Dashboard APIs
app.include_router(router)


# Home Route
@app.get("/")
def home():
    return {
        "product": "Project Atlas",
        "version": "1.0.0",
        "status": "Running",
        "message": "Welcome to the Future of AI Decision Intelligence"
    }