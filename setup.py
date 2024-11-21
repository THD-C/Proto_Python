from setuptools import setup, find_packages
import cfg
setup(
    name="THDC_PROTO",
    version=cfg.version,
    packages=find_packages(),
    author="THDC",
    author_email="thdc.p.lodz@outlook.com",
    description="gRPC protocol for THD-C project",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/THD-C/Protocol.git",
    python_requires='>=3.10',
    package_data={
        '': ['THDC_PROTO/**/*'],
    },
    include_package_data=True,
)
