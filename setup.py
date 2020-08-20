#!/usr/bin/env python
# -*- coding: utf-8 -*-

# setup.py
# Jim Bagrow
# Last Modified: 2020-08-19

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Jupyter Status",
    version="0.11",
    author="Jim Bagrow",
    author_email="bagrowjp@gmail.com",
    description="A quick, tabular summary of running Jupyter servers and kernels",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bagrow/jupyter-status",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'tabulate'
    ],
    entry_points = {
        'console_scripts' : ['jupyter-status=jupyter_status:main']
    }
)
