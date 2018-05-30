from setuptools import setup
from icinga2client import __author__, \
                          __author_email__, \
                          __desc__, \
                          __license__, \
                          __pkg_name__, \
                          __version__


setup(
    author=__author__,
    author_email=__author_email__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.5',
      ],
    description=__desc__,
    entry_points = {
        'console_scripts': ['i2c=icinga2client.cli:run'],
    },
    extras_require={
        'dev': [
            'pylint'
        ]
    },
    install_requires=[
        'icinga2api==0.6.*',
        'python-cli-ui==0.7.*'
    ],
    keywords='icinga api cli client',
    license=__license__,
    long_description=open('README.md').read(),
    name=__pkg_name__,
    packages=[
        'icinga2client'
    ],
    url='https://github.com/moenka/icinga2client',
    version=__version__,
    zip_safe=False,
)

