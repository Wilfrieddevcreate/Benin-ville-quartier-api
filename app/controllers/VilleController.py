from app.models.ville import villes

def get_villes():
    """
    Renvoie la liste des villes.
    
    Returns:
    list: Une liste de dictionnaires, chaque dictionnaire correspondant  une ville.
    """
    return villes

def get_ville_by_id(ville_id: int):
    """
    Renvoie la ville correspondant  l'ID donn .

    Parameters:
    ville_id (int): L'ID de la ville.

    Returns:
    dict or None: Le dictionnaire correspondant  la ville, ou None si la ville n'existe pas.
    """
    for ville in villes:
        if ville["id"] == ville_id:
            return ville
    return None
