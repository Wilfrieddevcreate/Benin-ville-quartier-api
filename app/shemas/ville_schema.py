from pydantic import BaseModel

class QuartierSchema(BaseModel):
    id: int
    nom: str
    ville_id: int
