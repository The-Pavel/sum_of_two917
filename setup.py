from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='sum_of_two',
      description="Calculates a sum of two numbers",
      version="1.0.0",
      packages=find_packages(),
      install_requires=requirements)
