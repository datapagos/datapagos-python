from setuptools import setup, find_packages

setup(
    name='datapagos',
    version='0.1.0',
    description='DataPagos API - Python Client',
    packages=find_packages(),
    install_requires = ['requests >= 1.1.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7'
    ]
)