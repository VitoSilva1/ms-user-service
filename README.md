# ms-user-service

Servicio FastAPI que gestiona el **ciclo de vida de usuarios**: registro, listado, consulta individual y autenticación interna para el resto de microservicios. `ms-auth-service` delega en este servicio la verificación de credenciales.

## Características
- Persistencia MySQL mediante SQLAlchemy con el modelo `User` (`app/models/user_model.py`).
- Hash de contraseñas usando `passlib` y roles (`admin`/`user`) vía enumeraciones.
- Endpoint interno `/users/internal/authenticate` protegido por el header `X-Internal-Secret`.
- Creación opcional de administradores por defecto (`Admin Jose`, `Admin Victor`) con `ensure_default_admins`.

## Variables de entorno

| Variable | Descripción |
| --- | --- |
| `DATABASE_URL` | Cadena de conexión MySQL (por ejemplo `mysql+pymysql://fintrack_admin:password@db:3306/fintrack_db`). |
| `SECRET_KEY` | Usada para hashear contraseñas (compatibilidad con utilidades compartidas). |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Mantiene compatibilidad con módulos comunes (no se usa directamente aquí). |
| `INTERNAL_API_KEY` | Clave compartida con `ms-auth-service` para el endpoint interno. |

Ejemplo `.env`:
```
DATABASE_URL=mysql+pymysql://fintrack_admin:Vicente5150.@db:3306/fintrack_db
SECRET_KEY=change-this-secret
ACCESS_TOKEN_EXPIRE_MINUTES=30
INTERNAL_API_KEY=fintruck-internal
```

## Ejecución
```bash
cd BackendFinTrack/ms-user-service
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Con Docker:
```bash
cd BackendFinTrack/ms-user-service
docker compose up --build
```

## Endpoints
- `POST /users/register` / `POST /users/user`: crean usuarios (la ruta `/register` valida correos duplicados).
- `GET /users/`: lista todos los usuarios.
- `GET /users/{id}`: devuelve un usuario específico.
- `POST /users/internal/authenticate`: **uso interno**. Requiere `X-Internal-Secret` con el valor de `INTERNAL_API_KEY` y responde con `{ "id": 1, "role": "admin" }` si las credenciales son válidas.

Para iniciar sesión públicamente usa `ms-auth-service` (`POST /auth/login`), que internamente llamará a este microservicio.
