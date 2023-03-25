# Immagine di base
FROM node:14.17-alpine

# Setta la directory di lavoro all'interno del container
WORKDIR /usr/src/app

# Copia i file package.json e package-lock.json nella directory di lavoro
COPY package*.json ./

# Installa le dipendenze
RUN npm install

# Copia il resto dei file dell'app nella directory di lavoro
COPY . .

# Compila l'app
RUN npm run build --prod

# Imposta la porta di ascolto
ENV PORT=80

# Avvia l'applicazione
CMD ["npm", "run", "start", "--", "--host", "0.0.0.0", "--port", "80"]
