from setuptools import setup, find_packages

setup(
    name="shared",
    version="0.1.0",
    description="Shared models and utilities for the flite-log monorepo",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pydantic[email]>=2.0.0",
    ],
) 