# import os

# # Definir la estructura básica del proyecto
# structure = {
#     'src': ['lambda_function.py', 'utils.py', '__init__.py'],
#     'tests': ['test_lambda_function.py', '__init__.py'],
#     '.': ['requirements.txt', 'README.md', '.gitignore', 'template.yaml']
# }

# # Plantillas de código base
# lambda_function_code = '''def lambda_handler(event, context):
#     """
#     Función principal para AWS Lambda.
#     """
#     return {
#         'statusCode': 200,
#         'body': 'Hello from Lambda!'
#     }
# '''

# test_lambda_code = '''import unittest
# from src.lambda_function import lambda_handler

# class TestLambdaFunction(unittest.TestCase):

#     def test_lambda_handler(self):
#         event = {}
#         context = None
#         response = lambda_handler(event, context)
#         self.assertEqual(response['statusCode'], 200)

# if __name__ == '__main__':
#     unittest.main()
# '''

# gitignore_content = '''# Python
# __pycache__/
# *.pyc
# *.pyo
# *.pyd

# # Entornos virtuales
# venv/
# .env

# # Archivos de configuración
# .DS_Store
# '''

# readme_content = '''# Proyecto Lambda en Python
# Este proyecto contiene una implementación básica de AWS Lambda utilizando buenas prácticas de desarrollo.
# '''

# requirements_content = '''boto3
# pytest
# '''

# template_content = '''Resources:
#     MyLambdaFunction:
#     Type: AWS::Serverless::Function
#     Properties:
#         Handler: src/lambda_function.lambda_handler
#         Runtime: python3.9
#         CodeUri: .
# '''

# # Crear la estructura del proyecto
# def create_project(project_name):
#     if not os.path.exists(project_name):
#         os.mkdir(project_name)

#     # Crear subdirectorios y archivos
#     for folder, files in structure.items():
#         folder_path = os.path.join(project_name, folder)
#         if folder != '.':
#             os.makedirs(folder_path, exist_ok=True)
#         for file in files:
#             file_path = os.path.join(folder_path if folder != '.' else project_name, file)
#             with open(file_path, 'w') as f:
#                 if file == 'lambda_function.py':
#                     f.write(lambda_function_code)
#                 elif file == 'test_lambda_function.py':
#                     f.write(test_lambda_code)
#                 elif file == '.gitignore':
#                     f.write(gitignore_content)
#                 elif file == 'README.md':
#                     f.write(readme_content)
#                 elif file == 'requirements.txt':
#                     f.write(requirements_content)
#                 elif file == 'template.yaml':
#                     f.write(template_content)
#                 else:
#                     f.write('')

#     print(f"Proyecto '{project_name}' creado exitosamente.")

# # Crear el proyecto Lambda
# if __name__ == "__main__":
#     project_name = input("Ingresa el nombre del proyecto: ")
#     create_project(project_name)

###################################################################################################################
#<< CODIGO REFACTORIZADO CON AMAZON Q>>
# import pathlib
# from typing import Optional

# # File content dictionary
# file_content = {
#     'lambda_function.py': '''def lambda_handler(event, context):
#     """
#     Main function for AWS Lambda.
#     """
#     return {
#         'statusCode': 200,
#         'body': 'Hello from Lambda!'
#     }
# ''',
#     'test_lambda_function.py': '''import unittest
# from src.lambda_function import lambda_handler

# class TestLambdaFunction(unittest.TestCase):

#     def test_lambda_handler(self):
#         event = {}
#         context = None
#         response = lambda_handler(event, context)
#         self.assertEqual(response['statusCode'], 200)

# if __name__ == '__main__':
#     unittest.main()
# ''',
#     '.gitignore': '''# Python
# __pycache__/
# *.pyc
# *.pyo
# *.pyd

# # Virtual environments
# venv/
# .env

# # Configuration files
# .DS_Store
# ''',
#     'README.md': '# Python Lambda Project\nThis project contains a basic implementation of AWS Lambda using best development practices.',
#     'requirements.txt': 'boto3\npytest',
#     'template.yaml': '''Resources:
#     MyLambdaFunction:
#     Type: AWS::Serverless::Function
#     Properties:
#         Handler: src/lambda_function.lambda_handler
#         Runtime: python3.9
#         CodeUri: .
# '''
# }

# # Project structure
# structure = {
#     'src': ['lambda_function.py', 'utils.py', '__init__.py'],
#     'tests': ['test_lambda_function.py', '__init__.py'],
#     '.': ['requirements.txt', 'README.md', '.gitignore', 'template.yaml']
# }


#     """
#     Create a project structure for an AWS Lambda function.

#     Args:
#         project_name (str): The name of the project.
#         project_path (pathlib.Path, optional): The path where the project should be created.
#             If not provided, the project will be created in the current working directory.
#     """
#     project_path = project_path or pathlib.Path.cwd()
#     project_dir = project_path / project_name

#     if not project_dir.exists():
#         project_dir.mkdir()

#     for folder, files in structure.items():
#         folder_path = project_dir / folder
#         if folder != '.':
#             folder_path.mkdir(parents=True, exist_ok=True)
#         for file in files:
#             file_path = folder_path / file if folder != '.' else project_dir / file
#             with file_path.open('w', encoding='utf-8') as f:
#                 f.write(file_content.get(file, ''))

#     print(f"Project '{project_name}' created successfully.")


# if __name__ == "__main__":
#     project_name = input("Enter the project name: ")
#     create_project(project_name)
###################################################################################################################
import os
from pathlib import Path
# Definir la estructura básica del proyecto
structure = {
    'src': ['lambda_function.py', 'utils.py', '__init__.py'],
    'tests': ['test_lambda_function.py', '__init__.py'],
    '.': ['requirements.txt', 'README.md', '.gitignore', 'template.yaml']
}

# Plantillas de código base
lambda_function_code = '''def lambda_handler(event, context):
    """
    Función principal para AWS Lambda.
    """
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
'''

test_lambda_code = '''import unittest
from src.lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def test_lambda_handler(self):
        event = {}
        context = None
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)

if __name__ == '__main__':
    unittest.main()
'''

gitignore_content = '''# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Entornos virtuales
venv/
.env

# Archivos de configuración
.DS_Store
'''

readme_content = '''# Proyecto Lambda en Python
Este proyecto contiene una implementación básica de AWS Lambda utilizando buenas prácticas de desarrollo.
'''

requirements_content = '''boto3
pytest
'''

template_content = '''Resources:
    MyLambdaFunction:
    Type: AWS::Serverless::Function
    Properties:
        Handler: src/lambda_function.lambda_handler
        Runtime: python3.9
        CodeUri: .
'''

# Crear la estructura del proyecto
def create_project(project_name):
    if not os.path.exists(project_name):
        os.mkdir(project_name)
    project_path = Path(project_name)
    # Crear subdirectorios y archivos
    file_contents = {
        'lambda_function.py': lambda_function_code,
        'test_lambda_function.py': test_lambda_code,
        '.gitignore': gitignore_content,
        'README.md': readme_content,
        'requirements.txt': requirements_content,
        'template.yaml': template_content
    }

    for folder, files in structure.items():
        folder_path = project_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        for file in files:
            file_path = folder_path / file
            file_path.write_text(file_contents.get(file, ''))

    print(f"Proyecto '{project_name}' creado exitosamente.")

# Crear el proyecto Lambda
if __name__ == "__main__":
    project_name = input("Ingresa el nombre del proyecto: ")
    create_project(project_name)
