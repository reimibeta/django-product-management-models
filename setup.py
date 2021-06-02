#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# if __name__ == "__main__":
import setuptools

setuptools.setup(
    name='product_management_models',
    version='1.0.7',
    packages=setuptools.find_packages(),
    install_requires=[
        # 'image-utils @ git+https://github.com/reimibeta/django-image-utils.git',
        # 'datetime-utils @ git+https://github.com/reimibeta/django-datetime-utils.git',
        # 'html-render-utils @ git+https://github.com/reimibeta/django-html-render-utils.git',
        # 'djangorestframework==3.12.4',
        # 'djangorestframework-simplejwt==4.7.0',
        # 'drf-flex-fields==0.9.0',
        # 'django-admin-list-filter-dropdown==1.0.3',
        # 'rest-framework-utils @ git+https://github.com/reimibeta/django-rest-framework-utils.git',
        'product-models @ git+https://github.com/reimibeta/django-product-models.git@a36b7e35037024670be725e055c3b007e2235cc9',
        # 'pillow==8.2.0',
        # 'django-cleanup==5.2.0',
        'supplier-models @ git+https://github.com/reimibeta/django-supplier-models.git@40b6bf354baeae7608bd6689585c68ef6f4f6d66',
    ]
    # scripts=['makemigrations.py','migrate.py']
)
