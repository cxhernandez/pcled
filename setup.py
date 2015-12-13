"""PCLED: Control your Arduino's LED strip through your PC"""
import sys
from glob import glob
from setuptools import setup, find_packages

NAME = "pcled"
VERSION = "0.1"


def read(filename):
    import os
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r') as fi:
        return fi.read()


def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)

# if we are running on python 3, enable 2to3 and
# let it use the custom fixers from the custom_fixers
# package.
extra = {}
if sys.version_info >= (3, 0):
    extra.update(
        use_2to3=True,
    )

setup(
    name=NAME,
    version=VERSION,
    description=("PCLED allows you to control your Arduino's "
                 "LED strip through your PC."),
    long_description=read('README.rst'),
    platforms=(
        "Windows", "Linux", "Mac OS-X", "Unix",
    ),
    classifiers=(
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering',
    ),
    keywords='led arduino',
    author="Carlos Xavier Hernandez",
    author_email="cxh@stanford.edu",
    url='https://github.com/cxhernandez/%s' % NAME,
    download_url='https://github.com/cxhernandez/%s/tarball/master' % NAME,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['README.rst',
             'requirements.txt'],
    },
    zip_safe=True,
    scripts=glob('./scripts/python/*.py'),
    install_requires=readlist('requirements.txt'),
    **extra
)
