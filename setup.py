from setuptools import setup

setup(name='openapi-typed',
      version='0.0.0',
      description='TypedDict typings for OpenAPI specification',
      url='http://github.com/unmock/openapi-typed',
      author='Meeshkan',
      author_email='dev@meeshkan.com',
      license='MIT',
      packages=['openapi_typed'],
      install_requires=[
          'typing-extensions',
      ],
      zip_safe=False)
