import sys

from setuptools import setup

from expyct import __version__

if sys.version_info == (3, 6):
    INSTALL_REQUIRES = ["dataclasses"]
else:
    INSTALL_REQUIRES = []

if __name__ == "__main__":
    setup(version=__version__, install_requires=INSTALL_REQUIRES)
