# ms-user-service

## Descripción

`ms-user-service` es un microservicio REST construido con FastAPI para la gestión de usuarios. Proporciona endpoints para crear, leer, actualizar y eliminar usuarios, inicialización automática de tablas en la base de datos al arrancar, y un mecanismo para asegurar la existencia de usuarios administradores por defecto.

El servicio está pensado para integrarse como un componente en una arquitectura de microservicios y está organizado por capas (rutas, servicios, modelos y esquemas) para mantener una separación clara de responsabilidades.

## Arquitectura y componentes principales

- **Punto de entrada**: `app/main.py` — instancia de FastAPI, middleware y eventos de arranque.
- **Rutas API**: `app/api/routes/users_routes.py` — definición de las rutas HTTP relacionadas con usuarios.
- **Lógica de negocio**: `app/services/user_service.py` — operaciones y reglas de negocio sobre usuarios (p. ej. asegurar administradores por defecto).
- **Modelos**: `app/models/user_model.py` — definiciones ORM con SQLAlchemy.
- **Esquemas**: `app/schemas/user_schema.py` — modelos de Pydantic usados para validación y serialización.
- **Core**: `app/core/config.py`, `app/core/database.py`, `app/core/security.py` — configuración, conexión a la BD y utilidades de seguridad (hash de contraseñas, etc.).

## Estructura de archivos

Raíz del proyecto (relevante):

- `Docker-compose.yml`
- `Dockerfile`
- `README.md`
- `requirements.txt`
- `app/main.py`
- `app/api/routes/users_routes.py`
- `app/core/config.py`
- `app/core/database.py`
- `app/core/security.py`
- `app/models/user_model.py`
- `app/schemas/user_schema.py`
- `app/services/user_service.py`

## Cómo ejecutar (local)

1. Crear y activar un entorno virtual (opcional pero recomendado):

```powershell
# Windows PowerShell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux (bash, zsh)
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```powershell
# Windows PowerShell
pip install -r requirements.txt
```

```bash
# macOS / Linux
pip3 install -r requirements.txt
```

3. Configurar variables de entorno necesarias (por ejemplo cadena de conexión a la BD). Revisar `app/core/config.py` para claves esperadas.

4. Ejecutar la aplicación en modo desarrollo:

```powershell
# Windows PowerShell
uvicorn app.main:app --reload
```

```bash
# macOS / Linux
uvicorn app.main:app --reload
```

Al iniciar, el servicio intentará crear las tablas de la base de datos y ejecutar los procesos de inicialización (por ejemplo, creación de administradores por defecto).

## Ejecutar con Docker

Revisar `Dockerfile` y `Docker-compose.yml` para los servicios y variables requeridas. Un flujo típico:

```powershell
# Windows PowerShell
docker-compose up --build
```

```bash
# macOS / Linux
docker-compose up --build
```

## Notas importantes

- **CORS**: se configura en `app/main.py`. Ver variable `BACKEND_CORS_ORIGINS` para orígenes permitidos.
- **Reintentos de conexión**: la creación de tablas contempla reintentos ante errores de conexión (útil cuando la BD arranca junto al contenedor).
- **Seguridad**: hashing de contraseñas y utilidades definidas en `app/core/security.py`. Revisar y adaptar algoritmos y parámetros a producción.

## Endpoints básicos

- `GET /` — punto raíz que indica que el servicio está en ejecución (ver `app/main.py`).
- Rutas de usuario definidas en `app/api/routes/users_routes.py` — revisar ese archivo para conocer los endpoints exactos (p. ej. `GET /users`, `POST /users`, etc.).

## Contribuciones y pruebas

- La organización por capas facilita pruebas unitarias y de integración. Para añadir pruebas, crea un entorno de pruebas con una base de datos aislada (SQLite en memoria o contenedor) y usa sesiones de la fábrica en `app/core/database.py`.
- Mantener el estilo y las convenciones del proyecto cuando se añadan rutas o servicios.

## Contacto y mantenimiento

Si necesitas ayuda para desplegar, añadir autenticación avanzada, o integrar con otros servicios, abre un issue o contacta al mantenedor del repositorio.

---

Archivo generado y actualizado automáticamente por el equipo de desarrollo.
