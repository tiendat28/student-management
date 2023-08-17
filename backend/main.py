from fastapi import  FastAPI

from config.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from endpoint import api


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api.api_router)

