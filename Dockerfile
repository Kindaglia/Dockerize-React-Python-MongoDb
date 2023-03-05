FROM python:3.9-slim-buster

WORKDIR /app

COPY Backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Backend/ .

CMD ["python", "app.py"]
