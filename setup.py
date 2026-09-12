from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gullfaxi-hcon",
    version="0.1.0",
    author="Leonard Haasbroek",
    author_email="leonardfhaasbroek@gmail.com",
    description="GullfaxiHCON - Fast dictionary-based BAM impact sensitivity (H50) prediction from SMILES",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={
        'gullfaxi': [
            'docs/*.md',
        ],
    },
    include_package_data=True,
    install_requires=[
        "rdkit>=2023.03.1",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "tqdm>=4.62.0",
        "scipy>=1.8.0",
    ],
    python_requires=">=3.8",
    license="BSD-3-Clause",
    license_files=["LICENSE"],
    project_urls={
        "Source": "https://github.com/LeonardFH/gullfaxi-hcon",
        "Bug Reports": "https://github.com/LeonardFH/gullfaxi-hcon/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: BSD License",
    ],
    entry_points={
        "console_scripts": [
            # Uncomment when CLI is ready
            # "gullfaxi-train=gullfaxi.train:main",
            # "gullfaxi-predict=gullfaxi.cli:main",
        ],
    },
)