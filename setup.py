# setup.py
from setuptools import find_packages, setup

setup(
    name="d1client",
    version="0.1.0",
    description="A client for interacting with Cloudflare D1 databases",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Stephane Busso",
    author_email="stephane.busso@gmail.com",
    url="https://github.com/yourusername/d1databaseclient",
    packages=find_packages(),
    install_requires=[
        "cloudflare",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
