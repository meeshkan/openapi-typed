from setuptools import find_packages, setup, Command
from shutil import rmtree
import os
import sys

# Package meta-data.
NAME = 'openapi_typed'
DESCRIPTION = 'TypedDict typings for OpenAPI specification'
URL = 'http://github.com/unmock/openapi-typed'
EMAIL = 'dev@meeshkan.com'
AUTHOR = 'Meeshkan Dev Team'
REQUIRES_PYTHON = '>=3.6.0'
SRC_DIR = 'openapi_typed'  # Relative location wrt setup.py

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

REQUIRED = [
    'typing-extensions'
]

DEV = [
    'mypy',
    'pytest',
    'setuptools',
    'twine',
    'wheel',
    'typeguard'
]

VERSION = '0.1.0'

# Optional packages
EXTRAS = {'dev': DEV}


class SetupCommand(Command):
    """Base class for setup.py commands with no arguments"""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def rmdir_if_exists(self, directory):
        self.status("Deleting {}".format(directory))
        rmtree(directory, ignore_errors=True)


def build():
    return os.system(
        "{executable} setup.py sdist bdist_wheel --universal".format(executable=sys.executable))


class BuildDistCommand(SetupCommand):
    """Support setup.py upload."""
    description = "Build the package."

    def run(self):
        self.status("Removing previous builds...")
        self.rmdir_if_exists(os.path.join(here, 'dist'))

        self.status("Building Source and Wheel (universal) distribution...")
        build()
        sys.exit()


def type_check():
    return os.system("pyright --lib")


class TypeCheckCommand(SetupCommand):
    """Run type-checking."""
    description = "Run type-checking."

    def run(self):
        sys.exit(type_check())


class UploadCommand(SetupCommand):
    """Support setup.py upload."""
    description = "Build and publish the package."

    def run(self):

        self.status("Removing previous builds...")
        self.rmdir_if_exists(os.path.join(here, 'dist'))

        self.status("Building Source and Wheel (universal) distribution...")
        exit_code = build()

        if exit_code != 0:
            sys.exit(exit_code)

        self.status("Uploading the package to PyPI via Twine...")
        exit_code = os.system("twine upload dist/*")

        if exit_code != 0:
            sys.exit(exit_code)

        self.status("Pushing git tags...")
        os.system("git tag v{about}".format(about=VERSION))
        exit_code = os.system("git push --tags")

        sys.exit(exit_code)


class TestCommand(SetupCommand):
    """Support setup.py test."""
    description = "Run local test if they exist"

    def run(self):
        os.system("pytest")
        sys.exit()


setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type='text/markdown',
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,
      python_requires=REQUIRES_PYTHON,
      license='MIT',
      packages=['openapi_typed'],
      include_package_data=True,
      package_data={
          'openapi_typed': ['py.typed']
      },
      install_requires=REQUIRED,
      extras_require=EXTRAS,
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      zip_safe=False,
      cmdclass={'dist': BuildDistCommand,
                'upload': UploadCommand,
                'test': TestCommand,
                'typecheck': TypeCheckCommand
                }
      )
