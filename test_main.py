from fastapi.testclient import TestClient
from main import app

#instanciation du client de test
client = TestClient(app)

def test_read_root():
    """Vérifie le code HTTP 200 et la structure du JSON de la racine."""
    response = client.get("/")
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "online"
    assert data["framework"] == "FastAPI"
    assert "Hello" in data["message"]

def test_health_check():
    """Vérifie le endpoint de supervision /health."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"health": "ok"}

def test_not_found():
    """Vérifie qu'une route inexistante renvoie bien une 404."""
    response = client.get("/route-inexistante")
    assert response.status_code == 404