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
from os.path import join, dirname

with open(join(dirname(__file__), 'SQLRaw/version.py'), 'r') as f:
    exec(f.read())

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(
    name='SQLRaw',
    version='1.0.0',
    url='https://github.com/tarnasi/SQLRaw',
    license='MIT',
    author='Shahriyar Tarnasi',
    author_email='shahryar.tarnasi@gmail.com',
    description="SQLRaw is a Python package for reading and writing SQL databases without knowing about the commands "
                "of each databases.",
    long_description=open('README.md').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    tests_require=[
        'nose',
        'packaging'
    ],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
