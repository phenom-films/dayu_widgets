"""Describe the distribution to distutils."""

# Import third-party modules
import os
import sys
from setuptools import find_packages
from setuptools import setup

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
README_PATH = os.path.join(ROOT_PATH, 'README.md')

if sys.version_info > (3, 0):
    requires = [
        'QT.py >= 1.3, <2',
        'six >=1.16,<2',
        'PySide2 >=5.5',
        'six >=1.16,<2',
        'dayu_path >=0.5.0'
    ]
else:
    requires = [
        'QT.py >= 1.3, <2',
        'six >=1.16,<2',
        'PySide >=1.2',
        'six >=1.16,<2',
        'dayu_path >=0.5.0'
    ]

setup(
    name='dayu_widgets',
    author='muyr',
    url='https://github.com/phenom-films/dayu_widgets',
    license='MIT',
    version='0.0.1',
    author_email='muyr@phenom-films.com',
    description=('Components for PySide.'),
    long_description=open(README_PATH, 'r', encoding='UTF-8').read(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
