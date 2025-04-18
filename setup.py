
from setuptools import find_packages,setup  
from typing import List

HYPHEN_e_DOT = '-e.'

def get_requirements(file_path : str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HYPHEN_e_DOT in requirements:
            requirements.remove(HYPHEN_e_DOT)

        return requirements

setup(
    name = 'Fault detection',
    version = '0.0.1',
    author = 'Shomiya Chaturvedi',
    author_email = 'shomiyac18@gmailcom',
    install_requires = get_requirements('requirements.txt'),
    packages= find_packages()
)
