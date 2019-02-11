#!/usr/bin/env python
import os
import shutil
import sys
from setuptools import setup, find_packages
try:
    from pip._internal.req import parse_requirements
    install_reqs = parse_requirements('requirements.txt', session=False)
except ImportError:
    from pip.req import parse_requirements
    install_reqs = parse_requirements('requirements.txt')

VERSION = '1.0.0'

long_description = '''implementation of some algorithms from nonparametric statistics'''

excluded = []
reqs = [str(ir.req) for ir in install_reqs]

def exclude_package(pkg):
    for exclude in excluded:
        if pkg.startswith(exclude):
            return True
    return False

def create_package_list(base_package):
    return ([base_package] +
            [base_package + '.' + pkg
             for pkg
             in find_packages(base_package)
             if not exclude_package(pkg)])


setup_info = dict(
    # Metadata
    name='pyglet',
    version=VERSION,
    author='Sergey Romanov',
    author_email='xxsmotur@gmail.com',
    description='Cross-platform windowing and multimedia library',
    long_description=long_description,
    install_requires=reqs,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Statistics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)