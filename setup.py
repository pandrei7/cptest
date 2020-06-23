from setuptools import setup

setup(
  name='cptest',
  entry_points={
    'console_scripts': [
      'cptest=main:main'
    ]
  }
)
