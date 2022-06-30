from setuptools import setup, find_packages

setup(
    name="demo-sphinx",
    version="0.1.0",
    install_requires=[
        "sphinx",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
