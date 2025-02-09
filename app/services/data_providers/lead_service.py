from sqlalchemy.orm import Session
from app.domain.models.lead import Lead
from app.domain.dto.lead_dto import LeadProcessedDTO, LeadFilterDTO
from app.domain.mappers.lead_mapper import LeadMapper
from typing import List

class LeadService:
    def __init__(self, db: Session):
        self.db = db

    def insert_leads(self):
        """ Inserta leads de ejemplo en la base de datos """
        leads = [
            {"name": "Ana Salcedo", "location": "Medellín", "budget": 200000000},
            {"name": "Santiago Gallo", "location": "Medellín", "budget": 500000000},
            {"name": "Carlota Habib", "location": "Medellín", "budget": 650000000},
            {"name": "Pablo Sánchez", "location": "Bogotá", "budget": 350000000},
            {"name": "Andrés Arias", "location": "Bogotá", "budget": 150000000},
            {"name": "Andrés Limas", "location": "Bogotá", "budget": 450000000},
        ]

        for lead in leads:
            db_lead = Lead(**lead)
            self.db.add(db_lead)
        self.db.commit()

    def process_leads(self, filters: LeadFilterDTO) -> LeadProcessedDTO:
        """ Filtra, ordena y calcula el presupuesto total de los leads """
        query = self.db.query(Lead)
        if filters.get("location"):
            query = query.filter(Lead.location == filters["location"])
        if filters.get("min_budget") is not None:
            query = query.filter(Lead.budget >= filters["min_budget"])
        if filters.get("max_budget") is not None:
            query = query.filter(Lead.budget <= filters["max_budget"])
        
        leads = query.all()
        sorted_leads = sorted(leads, key=lambda x: x.budget, reverse=True)
        total_budget = sum(lead.budget for lead in leads)

        return LeadProcessedDTO(
            filtered_leads=LeadMapper.to_dto_list(sorted_leads),
            total_budget=total_budget
        )
