from fastapi import APIRouter
from app.models.schemas import LoginRequest, RegisterRequest, TokenResponse
from app.services import auth_service, jwt_service

router = APIRouter()

# Al hacer login, devuelve un codigo asociado al secret key del microapi
# este token tiene toda la info, por lo que no necesita validarse nuevamente
# esta configurado con una vida de 1h
@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    user = auth_service.authenticate_user(data)
    # Solo ponemos el email, pero puedo añadir más info al payload 
    token = jwt_service.create_access_token({"sub": user["email"]})
    return TokenResponse(token=token)

@router.post("/register", response_model=TokenResponse)
def register(data: RegisterRequest):
    auth_service.register_user(data)
    # Opcional: hacer login automático tras registrar
    token = jwt_service.create_access_token({"sub": data.email})
    return TokenResponse(token=token)
