# 1. Imagen base de Python ligera
FROM python:3.9-slim

# 2. Carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar tus archivos al contenedor
COPY . .

# 4. Comando para arrancar el juego
CMD ["python", "main.py"]