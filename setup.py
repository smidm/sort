#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

setup(
    author="Matěj Šmíd",
    author_email='m@matejsmid.cz',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Simple, online, and realtime tracking of multiple objects in a video "
                "sequence.",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    name='sort',
    packages=find_packages(include=['sort', 'sort.*']),
    url='https://github.com/smidm/sort',
    version='0.1.0',
)
