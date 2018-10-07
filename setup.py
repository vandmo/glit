from setuptools import setup, find_packages

with open('VERSION') as version_file:
    version = version_file.read().strip()

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='plit',
    version=version,
    url='https://github.com/vandmo/plit',
    license='Apache License 2.0',
    author='vandmo',
    author_email='mikael@vandmo.se',
    description='Clones sets of git repositories',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pyyaml'
    ],
    entry_points='''
        [console_scripts]
        plit=plit.cli:cli
    ''',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ]
)
