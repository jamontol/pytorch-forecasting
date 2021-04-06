import os
from setuptools import setup, find_packages

setup(
    name='pytorch-forecasting',
    version='0.0',
    author='Jan Beitner',
    description='Pytorch Forecasting aims to ease state-of-the-art timeseries forecasting with neural networks for both real-world cases and research alike. The goal is to provide a high-level API with maximum flexibility for professionals and reasonable defaults for beginners',
    long_description=read('README.md'),
    keywords='forecasting, time-series, pytorch-lightning, pytorch',
    license='MIT License',
    url='https://github.com/jamontol/pytorch-forecasting',
    packages=find_packages(),

)
