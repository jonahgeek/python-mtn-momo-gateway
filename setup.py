from setuptools import setup, find_packages

setup(
    name='momogateway',
    version='0.1.0',
    description='MTN Momo Gateway',
    author='Jonathan Mwebaze',
    author_email='jonahgeek@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
