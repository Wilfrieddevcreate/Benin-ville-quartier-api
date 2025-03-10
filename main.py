import os
import uvicorn
from fastapi import FastAPI
from app.routes.ville import router as ville_router
from app.routes.quartier import router as quartier_router

app = FastAPI()

# Ajouter les routes
app.include_router(ville_router, prefix="/api")
app.include_router(quartier_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API des villes et quartiers du Bénin"}

# Lancer le serveur uniquement si c'est exécuté localement (pas sur Vercel)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Prendre le port de l'environnement si disponible
    uvicorn.run(app, host="0.0.0.0", port=port)
