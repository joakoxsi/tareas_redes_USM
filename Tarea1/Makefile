# Define el interprete de Python, adaptándose al SO
PYTHON = python3
ifeq ($(OS),Windows_NT)
    PYTHON = py -3
endif

# Regla por defecto para iniciar todos los servicios
.PHONY: all
all: run

# Regla para iniciar todos los servicios
.PHONY: run
run:
	@echo "Iniciando todos los servicios..."
	@$(PYTHON) servicio1.py &
	@$(PYTHON) servicio2.py &
	@$(PYTHON) servicio3.py &
	@$(PYTHON) servicio4.py &
	@echo "Todos los servicios están en ejecución."

# Regla para limpiar los archivos temporales (archivos de texto del servicio 4)
.PHONY: clean
clean:
	@echo "Limpiando archivos temporales..."
	@rm -f mensaje_final_*.txt
	@echo "Limpieza completada."