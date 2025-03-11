from app.models.quartier import quartiers

def get_quartiers(ville_id: int):
    """
    Renvoie la liste des quartiers pour une ville donn e.
    
    Parameters:
    ville_id (int): L'ID de la ville.
    
    Returns:
    list: Une liste de dictionnaires, chaque dictionnaire correspondant  un quartier.
    """
    return [q for q in quartiers if q["ville_id"] == ville_id]
