from setuptools import setup, find_packages

setup(
    name='EDSA1',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Project',
    long_description=open('README.md').read(),
    url='https://github.com/Keshc108/EDSA1',
    author='Keshav Chetty',
    author_email='keshc108@gmail.com'
)
