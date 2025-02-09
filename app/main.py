from fastapi import FastAPI
from app.infraestructure.controller.lead_controller import router as lead_router
from app.core.database import init_db

# Inicializar la aplicación FastAPI
app = FastAPI(
    title="Lead Management API",
    description="API para la gestión de leads con filtrado, ordenamiento y cálculo de presupuestos.",
    version="1.0.0"
)

# Inicializar la base de datos al iniciar la aplicación
init_db()

# Registrar los controladores de la API
app.include_router(lead_router, prefix="/api", tags=["Leads"])

# Endpoint de bienvenida
@app.get("/", tags=["Health Check"])
def home():
    return {"message": "Lead Management API is running!"}
