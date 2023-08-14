from setuptools import setup, find_packages

setup(
    name='momogateway',
    version='0.1.0',
    description='MTN MOMO Gateway - a Python package that simplifies the process of interacting with the MTN Mobile Money (MoMo) API, making it easy to create API users, generate API keys, and obtain bearer tokens for secure transactions.',
    author='Jonathan Mwebaze',
    author_email='jonahgeek@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    url='https://github.com/jonahgeek/python-mtn-momo-gateway',
    project_urls={
        'Author': 'https://mwebaze.com',
    }
)
