from fastapi import FastAPI, Depends, HTTPException
from routes import Air
from fastapi.middleware.cors import CORSMiddleware
# from core import comments_models
# from core.comments_database import engine
# from routes import comments_routes
# from routes.comments_routes import router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Air.router)
# app.include_router(router, prefix="/api")
# comments_models.Base.metadata.create_all(bind=engine)

# @app.get("/")
# def get_comment():
#     return "hola, mundo"