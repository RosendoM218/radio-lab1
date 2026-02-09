from setuptools import setup, find_packages

setup(
    name = "radio-lab1",
    version = "0.1.0",
    author = "Rosendo Medina-Uribe",
    description = "installable package used in LAB1 of ASTRON121 at UC Berkeley",
    long_description = "This package contains the code for common functions that are commonly used in LAB1 of the radio astronomy course ASTRON121 offered at UC Berkeley.",
    url = "https://github.com/RosendoM218/ASTRON121_LAB1_Package.git",
    package_dir = {"": "src"},
    packages = find_packages(where = "src"),
    install_requires = ["numpy >= 1.21"],
    python_requires = ">=3.9"
)