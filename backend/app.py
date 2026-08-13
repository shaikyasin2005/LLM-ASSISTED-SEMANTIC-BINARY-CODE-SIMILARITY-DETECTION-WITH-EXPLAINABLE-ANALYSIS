from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.similarity_routes import similarity_router

app = FastAPI()


# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API router
app.include_router(similarity_router)