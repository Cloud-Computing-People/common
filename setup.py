from setuptools import setup

from common import __version__

setup(
    name='ccp_common',
    version=__version__,
    url='https://github.com/Cloud-Computing-People/common',
    author='Aakash Aanegola'
    py_modules=packages=find_packages(),
    install_requires=[
        'starlette',
        'pymysql',
        'fastapi',
        'pydantic'
    ]
)