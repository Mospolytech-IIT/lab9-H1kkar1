import uvicorn
from fastapi import FastAPI

from app.post.router import post_router
from app.user.router import user_router


app = FastAPI()


app.include_router(user_router)
app.include_router(post_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
        host="localhost",
        port=8000,
    )
