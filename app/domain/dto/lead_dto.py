from typing import TypedDict, Optional, List

class LeadBaseDTO(TypedDict):
    name: str
    location: str
    budget: float

class LeadCreateDTO(LeadBaseDTO):
    """DTO para crear un Lead."""
    pass

class LeadResponseDTO(TypedDict):
    """DTO para la respuesta de un Lead."""
    id: int
    name: str
    location: str
    budget: float

class LeadFilterDTO(TypedDict, total=False):  # ✅ `total=False` hace que todos sean opcionales
    """DTO para filtrar leads."""
    location: Optional[str]
    min_budget: Optional[float]
    max_budget: Optional[float]

class LeadProcessedDTO(TypedDict):
    """DTO para la respuesta del procesamiento de leads."""
    filtered_leads: List[LeadResponseDTO]
    total_budget: float
