from setuptools import setup, find_packages
from typing import List  # Fixed: List instead of list

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return list of requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='MLPROJECTS',
    version='0.0.1',
    author='Uttam Maurya',
    author_email="ummauryas2005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Fixed: 'requirements.txt' instead of 'requirement.txt'
)