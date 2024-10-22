from setuptools import setup, find_packages

setup(
    name='mytool',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'mytool=mytool.main:main',
        ],
    },
)
