from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from pydantic import BaseModel

# Definir el modelo de usuario
class Usuario(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=50)

    def __str__(self):
        return self.username

# Definir el esquema de usuario
class UsuarioSchema(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True

# Registrar el modelo con FastAPI
app = FastAPI()
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["__main__"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# Crear una ruta para crear un usuario
@app.post("/usuarios", response_model=UsuarioSchema)
async def crear_usuario(usuario: UsuarioSchema):
    usuario_obj = await Usuario.create(**usuario.dict())
    return usuario_obj

# Crear una ruta para leer un usuario por username
@app.get("/usuarios/{username}", response_model=UsuarioSchema, responses={404: {"model": HTTPNotFoundError}})
async def leer_usuario(username: str):
    try:
        usuario_obj = await Usuario.get(username=username)
        return usuario_obj
    except:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Crear una ruta para actualizar un usuario por username
@app.put("/usuarios/{username}", response_model=UsuarioSchema, responses={404: {"model": HTTPNotFoundError}})
async def actualizar_usuario(username: str, usuario: UsuarioSchema):
    try:
        usuario_obj = await Usuario.get(username=username)
        usuario_obj.username = usuario.username
        usuario_obj.password = usuario.password
        await usuario_obj.save()
        return usuario_obj
    except:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Crear una ruta para borrar un usuario por username
@app.delete("/usuarios/{username}", response_model=UsuarioSchema, responses={404: {"model": HTTPNotFoundError}})
async def borrar_usuario(username: str):
    try:
        usuario_obj = await Usuario.get(username=username)
        await usuario_obj.delete()
        return usuario_obj
    except:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
