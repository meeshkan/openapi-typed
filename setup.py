from setuptools import setup

setup(name='openapi-typed',
      version='0.0.0',
      description='The funniest joke in the world',
      url='http://github.com/unmock/openapi-typed',
      author='Mike Solomon',
      author_email='mike@meeshkan.com',
      license='MIT',
      packages=['openapi_typed'],
      install_requires=[
          'typing-extensions',
      ],
      zip_safe=False)