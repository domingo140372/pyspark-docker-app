## Archivo para ejecucion de comandos comunes
.PHONY: build run test clean

build:
	docker build -t pyspark-truck-app:latest .

run:
	docker-compose up --build

test:
	pytest -q

clean:
	docker-compose down --rmi local --volumes --remove-orphans || true