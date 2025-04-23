import os

estructura_proyecto = {
    "README.md": "# Proyecto Python - RPA + ML\n\nEste proyecto integra un componente de RPA y otro de consumo de modelos de machine learning.",
    ".gitignore": "__pycache__/\n*.pyc\n.env\n",
    "requirements.txt": "# Aquí se listan las dependencias del proyecto\n# Ejemplo: requests, scikit-learn, pandas",
    "rpa": {
        "__init__.py": "",
        "main_rpa.py": "# Lógica principal de RPA",
        "utils_rpa.py": "# Funciones de utilidad para el módulo RPA"
    },
    "ml_service": {
        "__init__.py": "",
        "predict.py": "# Código para hacer predicciones con el modelo ML",
        "model_loader.py": "# Cargar el modelo ML",
        "data_preprocessing.py": "# Funciones de preprocesamiento de datos"
    },
    "config": {
        "__init__.py": "",
        "settings.py": "# Variables de configuración global del proyecto"
    },
    "tests": {
        "__init__.py": "",
        "test_rpa.py": "# Tests unitarios para módulo RPA",
        "test_ml_service.py": "# Tests unitarios para módulo ML"
    },
    "scripts": {
        "run_all.py": "# Script para ejecutar el proceso completo RPA + ML"
    }
}

def crear_estructura(base_path, estructura):
    """Crea recursivamente una estructura de carpetas y archivos."""
    for nombre, contenido in estructura.items():
        ruta = os.path.join(base_path, nombre)
        if isinstance(contenido, dict):
            os.makedirs(ruta, exist_ok=True)
            crear_estructura(ruta, contenido)
        else:
            with open(ruta, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)

def generar_proyecto(nombre_proyecto):
    base_path = os.path.abspath(nombre_proyecto)
    os.makedirs(base_path, exist_ok=True)
    crear_estructura(base_path, estructura_proyecto)
    print(f"✅ Proyecto generado en: {base_path}")

# Ejecutar
if __name__ == "__main__":
    nombre = input("Ingrese el nombre del proyecto: ")
    generar_proyecto(nombre)
