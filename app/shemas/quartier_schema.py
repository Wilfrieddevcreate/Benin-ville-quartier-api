from pydantic import BaseModel

class VilleSchema(BaseModel):
    id: int
    nom: str