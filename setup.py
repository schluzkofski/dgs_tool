import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="dgs_tool",
    version="0.0.1",
    description="Creating PV feed-in plots.",
    url="",
    author="Reiner Lemoine Institute",
    author_email="",
    license="MIT",
    packages=find_packages(),
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    zip_safe=False,
    install_requires=[
        "feedinlib == 0.1.0rc3",
        "jupyter"
    ],
)
