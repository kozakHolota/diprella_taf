from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="Diprella Testing Framework",
    version="1.0.1",
    author="Pavlo Mryhlotskyi",
    author_email="kozak_holota@gmail.com",
    install_requires = requirements,
)