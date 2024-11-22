from setuptools import setup, find_packages

setup(
    name="NordAnaStruct",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List dependencies from requirements.txt
    ],
    author="Nording",
    author_email="",
    description="Forked version of Anastruct with little fix",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Structtools/atHomeanaStruct",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)