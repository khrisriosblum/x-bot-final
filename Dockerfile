# Usar una imagen base de Python slim para reducir el tamaño
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar requirements.txt primero y instalar dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Ejecutar la aplicación FastAPI con Uvicorn en el puerto 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


