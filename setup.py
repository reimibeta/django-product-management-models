#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# if __name__ == "__main__":
import setuptools

setuptools.setup(
    name='product_management_models',
    version='1.1.2',
    packages=setuptools.find_packages(),
    # install_requires=[
    #     'product-models @ git+https://github.com/reimibeta/django-product-models.git',
    #     'supplier-models @ git+https://github.com/reimibeta/django-supplier-models.git',
    # ]
)
