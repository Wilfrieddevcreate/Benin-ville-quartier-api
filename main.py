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
