from typing import Protocol
from app.domain.dto.lead_dto import LeadCreateDTO, LeadFilterDTO, LeadProcessedDTO

class LeadPort(Protocol):
    def insert_leads(self, leads: list[LeadCreateDTO]) -> None:
        """Inserta leads en la base de datos a partir de una lista de DTOs."""
        pass

    def process_leads(self, filters: LeadFilterDTO) -> LeadProcessedDTO:
        """Filtra, ordena y calcula el presupuesto total de los leads."""
        pass
