import setuptools

with open("README.md", mode="r", encoding="utf-8") as file:
    readme_md = file.read().splitlines()

with open("requirements.txt", mode="r", encoding="utf-8") as file:
    dependency_list = file.read().splitlines()

setuptools.setup(
    name="python_pip_test",
    version="0.0.1",
    description="테스트",
    long_description=readme_md,
    long_description_content_type="text/markdown",
    url="https://github.com/2021-hknu-cd-hate-speech-classfication/test",
    install_requires=dependency_list
)
