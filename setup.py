"""
    setup
    ~~~~
    SQLRaw is a simple extension for Python that allows us access to all
    SQL commands as string capabilities with change it with format
    function in Python.

    :copyright: (c) 2024 by Shahriyar Tarnasi.
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup, find_packages
setup(
    name='SQLRaw',
    version='1.0',
    packages=find_packages(),
    description="SQLRaw is a Python package for reading and writing SQL databases without knowing about the commands of each databases.",
    url='#',
    author='Shahriyar Tarnasi',
    author_email='shahryar.tarnasi@gmail.com',
    license='MIT',
    zip_safe=False
)
