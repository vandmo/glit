from setuptools import setup, find_packages

with open('VERSION') as version_file:
    version = version_file.read().strip()

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='glit',
    version=version,
    url='https://github.com/vandmo/glit',
    license='Apache License 2.0',
    author='vandmo',
    author_email='mikael@vandmo.se',
    description='Clones sets of git repositories',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        glit=glit.cli:cli
    ''',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ]
)
