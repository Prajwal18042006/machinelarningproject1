from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from a given file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='machinelearningproject1',
    version='0.0.1',
    author='prajwal',
    author_email='jprajwal050@gmail.com',
    packages=find_packages(),  # ← Note: added parentheses here
    install_requires=get_requirements('requirement.txt')  # fixed filename
)
