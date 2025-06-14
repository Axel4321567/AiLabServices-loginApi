from fastapi import APIRouter, HTTPException, status
from app.models.schemas import LoginRequest, RegisterRequest, TokenResponse

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    # Lógica mock (debes conectar con tu base de datos real después)
    if data.email == "test@test.com" and data.password == "1234":
        return TokenResponse(token="fake-jwt-token")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales incorrectas"
    )

@router.post("/register", response_model=TokenResponse)
def register(data: RegisterRequest):
    # Lógica mock de registro
    return TokenResponse(token="fake-jwt-token")
