from fastapi import FastAPI
from app.api.auth_routes import router as auth_router

app = FastAPI(
    title="Auth API",
    description="Microservicio de autenticación"
)
app.include_router(auth_router)
