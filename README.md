# FreshAir Backend

FreshAir Backend es una aplicación que proporciona información sobre la calidad del aire en diversas ciudades. Utiliza la API de WAQI para obtener datos en tiempo real.

## Tabla de Contenidos

1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Uso](#uso)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Swagger](#swagger)
6. [Créditos](#créditos)

## Requisitos

Antes de empezar, tienes que asegúrate de tener instalados los siguientes programas:

- Python 3.7 o superior

- Fastapi

- SQLAlchemy

- Uvicorn

## Instalación

Sigue estos pasos para instalar y configurar el entorno de desarrollo:

# Clona el repositorio
git clone https://github.com/polBarco/FreshAir---Backend.git

# Entra en el directorio del proyecto
cd FreshAir---Backend

# Instala las dependencias
pip install -r requirements.txt

En el caso que no tengas el archivo 'requirements.txt' puedes crearlo con el siguiente comando:

pip freeze > requirements.txt

## Uso

Para levantar el backend, utiliza el siguiente comando:

uvicorn main:app --reload

La aplicación estará disponible en http://localhost:8000

## Estructura del proyecto

El codigo esta estructurado de la siguente manera: 

- core/: Define la estructura de la base de datos de los comentarios y la creación de la tabla.
- routes/: Define las rutas de la API.
- schemas/: Define los modelos de datos.
- services/: Incluye la lógica de negoció y la comunicación con servicios externos.
- test/: Define los test de las funciones.
- main.py: Punto principal de la aplicación.
- README.md: Este archivo.
- requirements.txt: Lista de dependencia del proyecto.

## Swagger

La aplicación esta pensada para poder crear, leer, modificar i eliminar comentarios. Para visualizar estas funcionalidades podeis acceder al Swagger y los diferentes endpoints.

Accede a: http://localhost:8000/docs

## Créditos

Este proyecto utiliza datos de la API de WAQI.