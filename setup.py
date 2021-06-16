#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# if __name__ == "__main__":
import setuptools

setuptools.setup(
    name='product_management_models',
    version='1.0.9',
    packages=setuptools.find_packages(),
    install_requires=[
        'product-models @ git+https://github.com/reimibeta/django-product-models.git@9f8eeb4f6991cc3b2f56579859bb0c6a2c16ad0e',
        'supplier-models @ git+https://github.com/reimibeta/django-supplier-models.git@40b6bf354baeae7608bd6689585c68ef6f4f6d66',
    ]
)
