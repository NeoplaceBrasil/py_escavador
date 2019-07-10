# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages
import sys

VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = ".".join(map(str, VERSION))

f = open(join(dirname(__file__), "README"))
long_description = f.read().strip()
f.close()

install_requires = ["urllib3>=1.21.1"]
tests_require = [
    "requests>=2.0.0, <3.0.0",
    "nose",
    "coverage",
    "mock",
    "pyaml",
    "nosexcover",
]

# use external unittest for 2.6
if sys.version_info[:2] == (2, 6):
    install_requires.append("unittest2")

setup(
    name="py_escavador",
    description="Python client for Escavador",
    license="GLP 3.0",
    url="https://github.com/escavador/py_escavador",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__versionstr__,
    author="Ícaro Jerry",
    author_email="icarojerry@potelo.com.br",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=install_requires,
    test_suite="",
    tests_require=[],
    extras_require={
        "develop": tests_require + ["sphinx<1.7", "sphinx_rtd_theme"],
        "requests": ["requests>=2.4.0, <3.0.0"],
    },
)
