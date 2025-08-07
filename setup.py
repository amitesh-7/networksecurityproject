from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements()->List[str]:
    requirements_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!=HYPEN_E_DOT:
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements_list

setup(
    name="NetworkSecurity",
    version="0.0.0.1",
    author="Amitesh Vishwakarma",
    author_email="amiteshvishwakarma2006@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    description="A project for network security using machine learning",
)