from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='openapi-typed',
      version='0.0.0',
      description='TypedDict typings for OpenAPI specification',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/unmock/openapi-typed',
      author='Meeshkan',
      author_email='dev@meeshkan.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'typing-extensions',
      ],
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      zip_safe=False)
