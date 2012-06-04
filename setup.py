# -*- encoding: utf8 -*-
from setuptools import setup, find_packages

setup(
    name="django-postfix",
    version="0.1.a.dev",
    packages=find_packages(),
    install_requires=[
        'Django>=1.4',
    ],
    author="Mario César Señoranis Ayala",
    author_email="mariocesar.c50@gmail.com",
    description="",
    license="BSD",
    keywords="postfix mail django",
    url="http://bitbucket.org/creat1va/django-postfix",
    zip_safe=True,
)
