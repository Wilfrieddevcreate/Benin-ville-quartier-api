import os
from fastapi import FastAPI
from app.routes.ville import router as ville_router
from app.routes.quartier import router as quartier_router
import uvicorn

app = FastAPI()

# Ajouter les routes
app.include_router(ville_router, prefix="/api")
app.include_router(quartier_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API des villes et quartiers du Bénin"}

# Si ce fichier est exécuté directement (pour le développement local)
if __name__ == "__main__":
    # Le port est déterminé par la variable d'environnement PORT
    port = int(os.environ.get("PORT", 8000))  # Si aucune variable PORT n'est définie, utilise 8000 par défaut
    uvicorn.run(app, host="0.0.0.0", port=port)
