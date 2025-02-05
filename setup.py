import pathlib
from setuptools import find_packages, setup
import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding='utf-8')

# This call to setup() does all the work
setup(
    name="trankit",
    version=get_version("trankit/__init__.py"),
    description="Trankit: A Light-Weight Transformer-based Toolkit for Multilingual Natural Language Processing",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nlp-uoregon/trankit",
    author="NLP Group at the University of Oregon",
    author_email="thien@cs.uoregon.edu",
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(),
    include_package_data=True,
    #install_requires=['adapters>=0.1.1', 'transformers', 'numpy', 'protobuf', 'requests', 'torch>=1.6.0,<=1.11.0', 'tqdm>=4.27', 'langid==1.1.6', 'filelock', 'tokenizers>=0.7.0', 'regex != 2019.12.17', 'packaging', 'sentencepiece', 'sacremoses', 'six'],
    install_requires=['adapter-transformers==1.1.1', 'certifi==2020.12.5', 'chardet==4.0.0', 'click==7.1.2', 'filelock==3.0.12', 'idna==2.10', 'joblib==1.0.1', 'numpy==1.20.1', 'packaging==20.9', 'protobuf==3.15.5', 'pyparsing==2.4.7', 'regex==2020.11.13', 'requests==2.25.1', 'sacremoses==0.0.43', 'sentencepiece==0.1.91', 'six==1.15.0', 'tokenizers==0.7.0', 'torch==1.8.0', 'tqdm==4.58.0', 'typing-extensions==3.7.4.3', 'urllib3==1.26.3'],
    entry_points={
    },
)
