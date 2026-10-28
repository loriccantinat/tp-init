from fastapi import FastAPI

app = FastAPI(title="Lab Test WSL Docker")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Hello depuis l'API conteneurisée sous WSL 2 !",
        "framework": "FastAPI"
    }

@app.get("/health")
def health_check():
    return {"health": "ok"}