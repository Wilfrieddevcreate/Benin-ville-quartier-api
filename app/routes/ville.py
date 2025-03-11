from fastapi import APIRouter
from app.controllers.VilleController import get_villes, get_ville_by_id

router = APIRouter()

@router.get("/villes")
def read_villes():
    return get_villes()

@router.get("/villes/{ville_id}")
def read_ville(ville_id: int):
    ville = get_ville_by_id(ville_id)
    if ville:
        return ville
    return {"message": "Ville non trouvée"}

