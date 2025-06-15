# Utilise une image avec Java (pour Spark) et Python
FROM eclipse-temurin:17-jdk

# Installe Python et pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    apt-get clean

# Dossier de travail
WORKDIR /app

# Copie tous les fichiers du projet local dans le conteneur
COPY . /app

# Installe les dépendances Python
RUN pip install --break-system-packages pandas numpy pyspark==4.0.0

# Commande à exécuter au lancement du conteneur
CMD ["python", "script_analyse_votes.py"]
