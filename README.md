# ms-user-service

Microservicio responsable de la administración de usuarios (registro, listado y consulta). Todas las operaciones de autenticación fueron movidas a `ms-auth-service`.

## Variables de entorno

- `DATABASE_URL`: cadena de conexión a la base de datos MySQL.
- `SECRET_KEY`, `ACCESS_TOKEN_EXPIRE_MINUTES`: siguen presentes para compatibilidad, pero solamente `SECRET_KEY` es requerida para el hash de contraseñas.
- `INTERNAL_API_KEY`: clave compartida que utilizan otros microservicios (por ejemplo `ms-auth-service`) para validar credenciales mediante el endpoint interno.

Ejemplo de `.env` local:

```
DATABASE_URL=mysql+pymysql://fintrack_admin:Vicente5150.@db:3306/fintrack_db
SECRET_KEY=change-this-secret
ACCESS_TOKEN_EXPIRE_MINUTES=30
INTERNAL_API_KEY=fintruck-internal
```

## Endpoints

- `POST /users/user` y `POST /users/register`: crean usuarios nuevos (con validación de correo duplicado en `/register`).
- `GET /users/`: lista usuarios.
- `GET /users/{id}`: obtiene un usuario por id.
- `POST /users/internal/authenticate`: endpoint interno (no documentado en Swagger) que valida las credenciales y retorna el `id` y `role` del usuario cuando el encabezado `X-Internal-Secret` coincide con `INTERNAL_API_KEY`.

Para login utiliza `ms-auth-service` mediante `POST /auth/login`.

## Ejecución local

```bash
cd ms-user-service
uvicorn app.main:app --reload --port 8000
```

O bien con Docker Compose:

```bash
cd ms-user-service
docker compose up --build
```
