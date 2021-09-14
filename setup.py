from setuptools import setup, find_packages

setup(
    name='salesforce-chatter',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python Library for Salesforce Chatter',
    long_description=open('README.md').read(),
    install_requires=['requests==2.26.0'],
    url='https://github.com/swagup-com/salesforce-chatter',
    author='Dak Gonzalez',
    author_email='dak@swagup.com'
)