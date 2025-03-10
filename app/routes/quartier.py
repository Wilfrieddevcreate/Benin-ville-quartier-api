from fastapi import APIRouter
from app.controllers.QuartierController import get_quartiers

router = APIRouter()

@router.get("/quartiers/{ville_id}")
def read_quartiers(ville_id: int):
    return get_quartiers(ville_id)
