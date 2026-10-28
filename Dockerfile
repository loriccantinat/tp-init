#image de base pour python (sert à exécuter l'application)
FROM python:3.12-slim

#définit le répertoire de travail dans le conteneur
WORKDIR /app

#permet de ne pas créer de fichiers .pyc et d'afficher les logs en temps réel
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#copie et installe les dépendances du projet (depuis le fichier requirements.txt)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copie le reste du code source
COPY . .

#port d'écoute du serveur FastAPI
EXPOSE 8000

#établie les commandes d'exécution du serveur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]