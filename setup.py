from setuptools import setup, find_packages

# pip >=20
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements

# def parse_requirements(filename):
#     """
#     Parse dependencies from a requirements file.
#     """
#     lineiter = (line.strip() for line in open(filename))
#     return [line for line in lineiter if line and not line.startswith("#")]

pages_requirements = parse_requirements(
    "./docs/requirements.txt", session=PipSession())

print(
    type(pages_requirements), pages_requirements
)

setup(
    name="demo-sphinx",
    version="0.1.0",
    install_requires=[
    ],
    extras_require={
            "dev": ["black"]
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
