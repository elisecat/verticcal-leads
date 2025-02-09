# app/application/use_cases/lead_use_case.py - Caso de uso para Leads
from app.domain.ports.lead_port import LeadPort
from typing import Optional, List
from app.domain.models.lead import Lead

class LeadUseCase:
    def __init__(self, lead_port: LeadPort):
        self.lead_port = lead_port

    def insert_leads(self) -> None:
        """Ejecuta la inserción de leads en la base de datos."""
        self.lead_port.insert_leads()

    def get_filtered_leads(self, location: Optional[str] = None, min_budget: Optional[float] = None, max_budget: Optional[float] = None) -> List[Lead]:
        """Obtiene leads filtrados por ubicación y presupuesto."""
        return self.lead_port.filter_leads(location, min_budget, max_budget)

    def get_total_budget(self, leads: List[Lead]) -> float:
        """Calcula el presupuesto total de los leads filtrados."""
        return self.lead_port.calculate_total_budget(leads)

    def get_sorted_leads(self, leads: List[Lead]) -> List[Lead]:
        """Ordena los leads por presupuesto de mayor a menor."""
        return self.lead_port.sort_leads_by_budget(leads)

    def process_leads(self, location: Optional[str] = None, min_budget: Optional[float] = None, max_budget: Optional[float] = None) -> dict:
        """Obtiene los leads filtrados, ordenados y calcula el presupuesto total."""
        leads = self.lead_port.filter_leads(location, min_budget, max_budget)
        sorted_leads = self.lead_port.sort_leads_by_budget(leads)
        total_budget = self.lead_port.calculate_total_budget(leads)
        return {
            "filtered_leads": sorted_leads,
            "total_budget": total_budget
        }
