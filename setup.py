#!/usr/bin/env python

import os
import re
import codecs

from setuptools import setup, find_packages


cwd = os.path.abspath(os.path.dirname(__file__))

def read(filename):
    with codecs.open(os.path.join(cwd, filename), "rb", "utf-8") as h:
        return h.read()

metadata = read(os.path.join(cwd, "plant_disease_classification_models", "__init__.py"))

def extract_metaitem(meta):
    meta_match = re.search(r"""^__{meta}__\s+=\s+['\"]([^'\"]*)['\"]""".format(meta=meta),
                           metadata, re.MULTILINE)
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))

requirements = [
]

test_requirements = [
]

setup(
    name="plant_disease_classification_models",
    version=extract_metaitem("version"),
    license=extract_metaitem("license"),
    description=extract_metaitem("description"),
    long_description=(read("README.rst")),
    long_description_content_type="text/x-rst",
    author=extract_metaitem("author"),
    author_email=extract_metaitem("email"),
    maintainer=extract_metaitem("author"),
    maintainer_email=extract_metaitem("email"),
    url=extract_metaitem("url"),
    download_url=extract_metaitem("download_url"),
    packages=[
        "plant_disease_classification_models",
    ],
    package_dir={"plant_disease_classification_models": "plant_disease_classification_models"},
    package_data={
        "plant_disease_classification_models": ["models/*.pt"]
    },
    platforms=["Any"],
    python_requires=">=3.5",
    install_requires=requirements,
    setup_requires=[],
    tests_require=test_requirements,
    zip_safe=False,
    keywords="plant disease classification, models, convolutional neural networks, cnn, pytorch",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
