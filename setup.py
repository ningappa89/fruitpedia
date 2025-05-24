from setuptools import setup

setup(
    name='fruitpedia',
    version='0.1.1',
    description='A Python library for fruit information',
    packages=['fruitpedia'],
    entry_points={
        'console_scripts': [
            'fruitpedia=fruitpedia.cli:main'
        ]
    },
    install_requires=[],
)
