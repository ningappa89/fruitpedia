from setuptools import setup, find_packages

setup(
    name="fruitpedia",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fruitpedia=fruitpedia.cli:main"
        ]
    },
    author="Your Name",
    description="A CLI library with info about 100 fruits",
    license="MIT",
)
