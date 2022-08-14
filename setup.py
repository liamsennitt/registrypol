from setuptools import setup, find_packages


with open('README.md', 'r') as file:
    long_description = file.read()


setup(
    name='registrypol',
    version='1.0.0',
    author='Liam Sennitt',
    description='Windows Registry Policy parser and emitter for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LiamSennitt/registrypol',
    packages=find_packages()
)
