# Usa l'immagine ufficiale di Python come base
FROM python:3.8-slim-buster

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze del progetto
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutti i file dell'app nella directory di lavoro
COPY . .

# Imposta la porta su cui l'app sarà in ascolto
EXPOSE 80

# Comando per eseguire l'app
CMD ["python", "app.py"]
