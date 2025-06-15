import bcrypt
from pymongo import MongoClient
from app.core.config import settings
from app.models.schemas import LoginRequest, RegisterRequest
from fastapi import HTTPException, status

client = MongoClient(settings.mongo_uri)
db = client[settings.mongo_db]
users_collection = db["users"]

def register_user(data: RegisterRequest):
    # Valida formato mínimo de email y longitud de contraseña
    if "@" not in data.email or len(data.password) < 4:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email o contraseña no válidos"
        )
    # Comprueba si el usuario ya existe
    if users_collection.find_one({"email": data.email}):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Usuario ya registrado"
        )
    # Hashea la contraseña antes de guardar
    hashed_pw = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
    user = {"email": data.email, "password": hashed_pw.decode()}
    users_collection.insert_one(user)

def authenticate_user(data: LoginRequest):
    user = users_collection.find_one({"email": data.email})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    if not bcrypt.checkpw(data.password.encode(), user["password"].encode()):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    return user
