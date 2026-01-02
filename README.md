# PySpark Truck Traffic App (Docker + pytest)

Proyecto de ejemplo que procesa un dataset de tráfico de camiones y carga pesada en EE. UU.
Incluye Docker, docker-compose, pruebas unitarias con pytest y CI básico con GitHub Actions.

Contenido
- app/: código de la aplicación (main y transform)
- data/: dataset de ejemplo (CSV)
- tests/: pruebas unitarias con pytest
- Dockerfile, docker-compose.yml
- .github/workflows/ci.yml: CI que ejecuta tests y construye imagen
- Makefile: comandos útiles

Requisitos
- Docker
- docker-compose
- (opcional) gh CLI para crear repositorios: https://cli.github.com/
- Python 3.10+ si quieres correr tests localmente

Cómo ejecutar con Docker (demo)
1. Copia el repositorio a tu máquina.
2. Coloca/usa el CSV en data/input_truck_traffic.csv (ya incluido).
3. Levanta el contenedor:
   docker-compose up --build
   (esto ejecuta app/main.py que leerá INPUT_PATH y escribirá en OUTPUT_PATH)
4. Verifica output en data/output/

Ejecutar tests localmente
- pip install -r requirements.txt
- pytest -q
