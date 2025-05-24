from setuptools import setup

setup(

    name='fruitpedia',
    version='0.1.1',
    description='A Python library for fruit information',
    packages=['fruitpedia'],

    name="fruitpedia",
    version="0.1.1",
    author="Ningappa Kanavi",
    description="A Python library with information on 100 fruits and CLI support",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fruitpedia",
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'fruitpedia=fruitpedia.cli:main'
        ]
    },
    install_requires=[],
)
