from setuptools import setup, find_packages
from typing import List

project_name = 'src'
author = 'Jay Raja'
version = '0.1.0'
description = 'Scania trucks and buses brake system failure detection'

def read_packages() -> List[str]:
    with open('requirements.txt', 'r+') as file:
        packages = [package for package in file.readlines() if package != '-e .']
    return packages

setup(
    name = project_name,
    author = author,
    version = version,
    description = description,
    packages = find_packages(),
    install_requires = read_packages()
)