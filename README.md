# **README del Proyecto Verticcal Leads**

---

## **1. Información General**

### 1.1 Nombre del Microservicio
- **Nombre:** Verticcal Leads
- **Clasificación del Servicio:** Gestión de Leads
- **Versión Actual:** v1.0.0
- **Fecha de Publicación:** 08/02/2025
- **Propietario:** Equipo Verticcal

### 1.2 Propósito del Microservicio
- **Descripción:** Microservicio que permite gestionar leads, incluyendo su registro, filtrado, cálculo de presupuesto y ordenamiento. Ofrece endpoints RESTful para manejar datos relevantes de los leads.
- **Objetivo del Servicio:** Implementar funcionalidades para gestionar información de leads y generar estadísticas útiles para la toma de decisiones.
- **Usuarios Destinatarios:** Aplicaciones o microservicios que requieran gestión de leads.

---

## **2. Endpoints**

| Método | Endpoint           | Descripción                                           |
|--------|--------------------|-------------------------------------------------------|
| POST   | `/leads/init`      | Inserta leads de ejemplo en la base de datos.         |
| POST   | `/leads/`          | Filtra, ordena y calcula el presupuesto de los leads. |

---

### **2.1 POST /leads/init**
- **Descripción:** Inserta leads de ejemplo en la base de datos.
- **Autenticación Requerida:** No.
- **Cuerpo de la Solicitud:** *No aplica.*
  
#### **Ejemplo de Respuesta Exitosa:**
```json
{
  "message": "Leads insertados correctamente"
}
```

---

### **2.2 POST /leads/**
- **Descripción:** Filtra, ordena y calcula el presupuesto total de los leads.
- **Autenticación Requerida:** No.
- **Cuerpo de la Solicitud:**
```json
{
  "location": "Medellín",
  "min_budget": 200000000,
  "max_budget": 600000000
}
```

#### **Respuestas:**

**Respuesta Exitosa (200):**
```json
{
  "filtered_leads": [
    {"id": 2, "name": "Santiago Gallo", "location": "Medellín", "budget": 500000000},
    {"id": 1, "name": "Ana Salcedo", "location": "Medellín", "budget": 200000000}
  ],
  "total_budget": 700000000
}
```


---

## **3. Estructura del Proyecto**

```plaintext
📦app
 ┣ 📂application
 ┃ ┗ 📂use_cases
 ┃ ┃ ┗ 📜lead_use_case.py
 ┣ 📂core
 ┃ ┗ 📜database.py
 ┣ 📂domain
 ┃ ┣ 📂dto
 ┃ ┃ ┗ 📜lead_dto.py
 ┃ ┣ 📂mappers
 ┃ ┃ ┗ 📜lead_mapper.py
 ┃ ┣ 📂models
 ┃ ┃ ┗ 📜lead.py
 ┃ ┗ 📂ports
 ┃ ┃ ┗ 📜lead_port.py
 ┣ 📂infraestructure
 ┃ ┗ 📂controller
 ┃ ┃ ┗ 📜lead_controller.py
 ┣ 📂services
 ┃ ┗ 📂data_providers
 ┃ ┃ ┗ 📜lead_service.py
 ┗ 📜main.py
```

---

## **4. Configuración del Proyecto**

### **4.1 Variables de Entorno**
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```ini
DATABASE_URL=postgresql://username:password@localhost:5432/leads
```

### **4.2 Instalación**

1. Crear un entorno virtual e instalar las dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Define las variables de entorno necesarias
   ```bash
    DB_USER=postgres
    DB_PASSWORD=password
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=leads
   ```
 
3. Crea la tabla de base de datos con el script
  ```sql
    CREATE TABLE leads (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        budget NUMERIC(15, 2) NOT NULL
    );

    CREATE INDEX idx_leads_name ON leads(name);
    CREATE INDEX idx_leads_location ON leads(location);
    CREATE INDEX idx_leads_budget ON leads(budget);
  ```

4. Ejecutar el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```


## **5. Contacto y Soporte**
Para soporte técnico, contacta al equipo responsable del microservicio o envía un correo a **saraelissad@gmail.com**.

---
