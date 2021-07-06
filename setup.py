from setuptools import setup

with open("requirements.txt") as file:
    dependency_list = file.read().splitlines()

setup(
    name="python_pip_test",
    version="0.0.1",
    install_requires=dependency_list
)
