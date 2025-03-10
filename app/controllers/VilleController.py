from app.models.ville import villes

def get_villes():
    return villes

def get_ville_by_id(ville_id: int):
    for ville in villes:
        if ville["id"] == ville_id:
            return ville
    return None
