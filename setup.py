"""
Setup module for Pylint plugin for Django.
"""
from setuptools import setup, find_packages

setup(
    name='vintage',
    url='https://github.com/PyCQA/pylint-django',
    author='Shawn Shojaie',
    author_email='',
    description='',
    long_description='',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pylint<2.0',
    ],
    license='BSD',
    classifiers=[],
    keywords=['pylint', 'django', 'plugin'],
    zip_safe=False,
)
