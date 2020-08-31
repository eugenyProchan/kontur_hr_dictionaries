
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='download_dictionaries_to_hf',
    version='0.0.1',
    description=long_description,
    long_description=long_description,
    packages=find_packages(where='download_dictionaries_to_hf'),
)