import sys

from setuptools import setup

from expyct.__version__ import VERSION

if sys.version_info == (3, 6):
    INSTALL_REQUIRES = ["dataclasses"]
else:
    INSTALL_REQUIRES = []

if __name__ == "__main__":
    setup(version=VERSION, install_requires=INSTALL_REQUIRES)
