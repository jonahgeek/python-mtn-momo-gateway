from setuptools import setup, find_packages

setup(
    name='momogateway',
    version='0.1.1',
    description='MTN MOMO Gateway - simplifies the process of interacting with the MTN Mobile Money API, making it easy to create API users, generate API keys.',
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
