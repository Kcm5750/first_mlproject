from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Fixed typo in `readliines`
        requirements = [req.strip() for req in requirements]  # Strips all extra whitespace
        
        # Remove '-e .' if it exists
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='kcm5750',
    author_email='moulichandramouli81@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Fixed 'requirement.txt' typo
)
