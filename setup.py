from setuptools import find_packages, setup  
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        # Remove '-e .' if present
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='Fault detection',
    version='0.0.1',
    author='Shomiya Chaturvedi',
    author_email='shomiyac18@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
