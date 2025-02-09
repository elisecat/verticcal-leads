from app.domain.models.lead import Lead
from app.domain.dto.lead_dto import LeadResponseDTO
from typing import List

class LeadMapper:
    @staticmethod
    def to_dto(lead: Lead) -> LeadResponseDTO:
        """Convierte un objeto Lead (SQLAlchemy) en un DTO LeadResponseDTO manualmente."""
        return LeadResponseDTO(
            id=lead.id,
            name=lead.name,
            location=lead.location,
            budget=lead.budget
        )

    @staticmethod
    def to_dto_list(leads: List[Lead]) -> List[LeadResponseDTO]:
        """Convierte una lista de objetos Lead en una lista de DTOs LeadResponseDTO."""
        return [LeadMapper.to_dto(lead) for lead in leads]
