#what name and version our package have and which library needed

from distutils.core import setup
from setuptools import find_packages

setup(name='snowflakes',
      version='1.0.0',
      description='drawing random snowflakes',
      author='A. Setayesh',
      author_email='ardalan.setayesh@gmail.com',
      packages=find_packages(),
      install_requires=['numpy', 'turtles'],
     )