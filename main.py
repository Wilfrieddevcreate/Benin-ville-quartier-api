import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.ville import router as ville_router
from app.routes.quartier import router as quartier_router

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines (* = tous les domaines)
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les headers
)
# Ajouter les routes
app.include_router(ville_router, prefix="/api")
app.include_router(quartier_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API des villes et quartiers du Bénin"}

# Lancer le serveur uniquement si c'est exécuté localement 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Prendre le port de l'environnement si disponible
    uvicorn.run(app, host="0.0.0.0", port=port)
