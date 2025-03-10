from app.models.quartier import quartiers

def get_quartiers(ville_id: int):
    return [q for q in quartiers if q["ville_id"] == ville_id]
