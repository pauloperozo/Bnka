from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

@app.post("/users", response_model=UserSchema)
async def create_user(user: UserSchema):
    # Validar los datos con el esquema de Pydantic
    if await User.exists(username=user.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    if await User.exists(email=user.email):
        raise HTTPException(status_code=400, detail="Email already taken")
    
    # Crear el usuario en la base de datos con el modelo de Tortoise
    user_obj = await User.create(**user.dict())
    
    # Devolver los datos del usuario creado con el esquema de Pydantic
    return user_obj

# Registrar los modelos de Tortoise con FastAPI
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
