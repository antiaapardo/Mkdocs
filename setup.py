from setuptools import setup
import pathlib
 
# Carpeta raíz del proyecto
BASE_DIR = pathlib.Path(__file__).parent
 
# Leer el README
README = (BASE_DIR / "README.md").read_text()
 
setup(
    name="pypi_Antia",
    version="0.0.1",
    description="Hola mundo con PySide6",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Antia",
    author_email="pardojimenezantia@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=["pypi_Antia"],
    include_package_data=True,
    install_requires=["PySide6"],
    entry_points={
        "console_scripts": [
            "pypi_Antia=pypi_Antia.hola_mundo:main"
        ]
    },
)