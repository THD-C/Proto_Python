from setuptools import setup, find_packages
import cfg

setup(
    name="thdcgrpc",
    version="0.0.0",
    packages=find_packages(),
    author="THDC",
    author_email="thdc.p.lodz@outlook.com",
    description="gRPC protocol for THD-C project",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/THD-C/Proto_Python.git",
    python_requires='>=3.10',
    package_data={
        '': ['*'],
    },
    include_package_data=True,
)
