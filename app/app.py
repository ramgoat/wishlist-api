import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Ramgoat Wishlist API", description="Welcome to the Wishlist API!", version="0.2.0")

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8085)
