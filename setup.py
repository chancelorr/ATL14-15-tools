#! usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="ATL14-15-tools",                        # Package name
    version="0.1.1",                          # Version
    description="Tools for ATL14 and ATL15.",
    long_description=open("README.md").read(),  # Readme as long description
    long_description_content_type="text/markdown",
    author="Chance",
    author_email="ccroberts@ucsd.edu",
    url="https://github.com/chancelorr/ATL14-15-tools",  # Project URL
    packages=find_packages(),                 # Automatically find packages
    include_package_data=True,                # Include non-code files specified in MANIFEST.in
    install_requires=[                        # Dependencies
        "numpy>=1.21.0",
        "pandas>=1.3.0",
    ],
    classifiers=[                             # Optional metadata for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=[],
    python_requires=">=3.7",                  # Minimum Python version
)
