from setuptools import setup

from setuptools import find_packages

setup(
    name='ccp_common',
    version="0.1.0",
    url='https://github.com/Cloud-Computing-People/common',
    author='Aakash Aanegola',
    py_modules=find_packages(),
    install_requires=[
        'starlette',
        'pymysql',
        'fastapi',
        'pydantic'
    ]
)