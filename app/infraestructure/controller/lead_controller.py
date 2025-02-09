from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.data_providers.lead_service import LeadService
from app.core.database import SessionLocal
from app.domain.dto.lead_dto import LeadProcessedDTO, LeadFilterDTO

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/leads/init")
def initialize_leads(db: Session = Depends(get_db)):
    """ Endpoint para insertar los leads de ejemplo """
    service = LeadService(db)
    service.insert_leads()
    return {"message": "Leads insertados correctamente"}

@router.post("/leads/", response_model=LeadProcessedDTO)
def get_leads(filters: LeadFilterDTO, db: Session = Depends(get_db)):
    """ Endpoint para filtrar, ordenar y calcular el presupuesto total de leads """
    try:
        service = LeadService(db)
        return service.process_leads(filters)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
