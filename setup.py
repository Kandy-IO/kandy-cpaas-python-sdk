#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ 'requests>=2.22', 'PyJWT>=1.7.1' ]

current_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(current_dir, "kandycpaas", "__version__.py"), "r") as f:
    exec(f.read(), about)

setup(
    author="KeepWorks",
    author_email='kandy@keepworks.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python SDK for Kandy CPaaS",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='kandycpaas',
    name='kandycpaas',
    packages=find_packages(include=['kandycpaas']),
    version=about['__version__'],
    zip_safe=False
)
