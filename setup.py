# -*- encoding: utf8 -*-
from setuptools import setup, find_packages

with open('README.rst') as readme:
        long_description = readme.read()

setup(
    name="django-postfix",
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=['setuptools_scm',],
    install_requires=['distribute','Django>=1.4'],
    author="Mario César Señoranis Ayala",
    author_email="mariocesar.c50@gmail.com",
    description="A django app to manage postfix mailboxes",
    long_description=long_description,
    license="MIT License",
    keywords="postfix mail django",
    url="http://bitbucket.org/creat1va/django-postfix",
    zip_safe=True,
    classifiers=[
        'Development Status :: 1 - Planning',
       'Environment :: Web Environment',
       'Framework :: Django',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: MIT License',
       'Operating System :: OS Independent',
       'Programming Language :: Python',
       'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
